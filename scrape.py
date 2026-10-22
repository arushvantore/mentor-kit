#!/usr/bin/env python3
"""Mentor page capturer — saves web pages into materials/ for the AI.

SAFETY (read-only by design):
- YOU log in yourself; credentials stay in .browser-profile/ on this Mac
  (never committed to git, never read by the AI).
- This tool never types into forms, never clicks site buttons, never
  submits anything, never uploads anywhere. It only READS pages.
- Captures land as .md (page text) + .png (full screenshot) + log line.

Modes:
  interactive (default): python3 scrape.py <url> [url ...]
      Opens a visible window. You browse, you click the blue
      CAPTURE button on each page you want saved. Close window = done.
  automatic:             python3 scrape.py --auto
      Headless daily refresh. Opens each URL in targets.txt, checks you
      are still logged in, saves the visible (newest) content as
      auto_YYYYMMDD_*.md. If a session expired it logs ACTION NEEDED
      instead of saving a login page.
  selftest:              python3 scrape.py --selftest

Options:
  --auto               automatic refresh mode (uses targets.txt)
  --targets FILE       URL list for --auto (default: targets.txt next to script)
  --profile DIR        browser profile (default: .browser-profile)
  --windowed           run --auto in a visible window (debugging)
  --selftest           offline end-to-end check
"""

import re
import sys
import time
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE = Path(__file__).resolve().parent
MATERIALS = BASE / "materials"
PROFILE = BASE / ".browser-profile"
TEST_PROFILE = BASE / ".browser-profile-test"
LOGF = BASE / "captures.log"
DEFAULT_TARGETS = BASE / "targets.txt"

LOGIN_HINTS = ("signin", "login", "sso", "authorize", "oauth", "auth")

# Run inside the user's REAL Google Chrome (Google rejects sign-in in
# the "Chrome for Testing" build). Hide the automation tells so the
# portal's Google SSO accepts the login like a normal browser.
STEALTH_ARGS = [
    "--disable-blink-features=AutomationControlled",
    "--no-first-run",
    "--no-default-browser-check",
]
STEALTH_JS = """
Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
"""

# Injected into every top-level page: a big blue button (interactive mode).
# Clicking it only sets a flag in the page; Python reads the flag and saves.
INIT_JS = """
if (window.top === window) {
  const boot = () => {
    if (document.getElementById('mentor-capture-host')) return;
    if (!document.body) return;
    const host = document.createElement('div');
    host.id = 'mentor-capture-host';
    const root = host.attachShadow({ mode: 'open' });
    root.innerHTML = `
      <style>
        .b { position: fixed; right: 20px; bottom: 20px; z-index: 2147483647;
             background: #1a73e8; color: #fff; border: 0; border-radius: 26px;
             padding: 14px 24px; font-size: 15px; font-weight: 700;
             cursor: pointer; box-shadow: 0 6px 18px rgba(0,0,0,.4);
             font-family: -apple-system, sans-serif; }
        .b:active { transform: scale(.96); }
        .t { position: fixed; right: 20px; bottom: 76px; z-index: 2147483647;
             background: #0b6b33; color: #fff; padding: 8px 14px;
             border-radius: 8px; font-size: 13px;
             font-family: -apple-system, sans-serif; display: none;
             box-shadow: 0 4px 12px rgba(0,0,0,.35); }
      </style>
      <button class="b" type="button">&#128194; CAPTURE THIS PAGE</button>
      <div class="t">&#10003; saved to exam-prep/materials</div>`;
    document.body.appendChild(host);
    root.querySelector('.b').addEventListener('click', () => {
      window.__mentorWant = Date.now();
      const toast = root.querySelector('.t');
      toast.style.display = 'block';
      setTimeout(() => { toast.style.display = 'none'; }, 1800);
    });
  };
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
  document.addEventListener('click', () => setTimeout(boot, 500), true);
}
"""


def log(message):
    line = datetime.now().isoformat(timespec="seconds") + " " + message
    print(line, flush=True)
    with LOGF.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def slugify(text, limit=40):
    slug = re.sub(r"[^a-z0-9]+", "-", (text or "page").lower()).strip("-")
    return slug[:limit] or "page"


def read_text(page):
    return page.evaluate("() => (document.body ? document.body.innerText : '')")


def save(page, url, title, text, fixed_name=None):
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if fixed_name:
        stem = fixed_name
    else:
        stem = stamp + "_" + slugify(title)
    md_path = MATERIALS / (stem + ".md")
    counter = 1
    while md_path.exists() and not fixed_name:
        counter += 1
        md_path = MATERIALS / (stem + "_" + str(counter) + ".md")
    md_path.write_text(
        "# " + str(title) + "\n\nURL: " + str(url)
        + "\nCaptured: " + datetime.now().isoformat(timespec="seconds")
        + "\n\n---\n\n" + (text or "") + "\n",
        encoding="utf-8",
    )
    try:
        page.screenshot(path=str(md_path.with_suffix(".png")), full_page=True)
    except Exception as error:
        log("  screenshot skipped: " + str(error))
    log("SAVED " + md_path.name + "  <- " + str(url))


def extract(page, fixed_name=None):
    save(page, page.url, page.title(), read_text(page), fixed_name=fixed_name)


def looks_logged_out(page):
    try:
        if page.locator("input[type=password]").count() > 0:
            return True
        lower = page.url.lower()
        return any(hint in lower for hint in LOGIN_HINTS)
    except Exception:
        return False


# ---------------------------------------------------------------- interactive

def pump(context, seen):
    """One watcher cycle: notice page flag-clicks and save them."""
    try:
        current = list(context.pages)
    except Exception:
        return False
    if not current:
        return False
    for page in current:
        try:
            want = page.evaluate("window.__mentorWant || 0")
        except Exception:
            continue
        last = seen.get(id(page), 0)
        if want and want != last:
            seen[id(page)] = want
            try:
                extract(page)
            except Exception as error:
                log("ERROR capturing: " + str(error))
    return True


def watch(context):
    seen = {}
    while pump(context, seen):
        time.sleep(0.5)
    log("Browser closed. Everything captured.")


def run_interactive(urls, profile):
    MATERIALS.mkdir(exist_ok=True)
    with sync_playwright() as pw:
        context = pw.chromium.launch_persistent_context(
            str(profile), channel="chrome", headless=False, no_viewport=True,
            args=STEALTH_ARGS + ["--window-size=1400,900"],
        )
        context.add_init_script(STEALTH_JS + INIT_JS)
        try:
            pages = list(context.pages) or [context.new_page()]
            pages[0].goto(urls[0], wait_until="domcontentloaded", timeout=45000)
            for url in urls[1:]:
                page = context.new_page()
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=45000)
                except Exception as error:
                    log("note: could not load " + url + " (" + str(error)
                        + ") — open it manually in the window")
        except Exception as error:
            log("note: page load issue (" + str(error)
                + ") — the window is open, navigate manually")
        log("Browser ready. 1) Log in yourself if asked. 2) Open the pages "
            "you want. 3) Click the blue CAPTURE button on each. "
            "4) Close the window to finish.")
        try:
            watch(context)
        except KeyboardInterrupt:
            log("Interrupted by user.")
        finally:
            try:
                context.close()
            except Exception:
                pass


# ------------------------------------------------------------------ automatic

def run_auto(targets, profile, windowed=False):
    MATERIALS.mkdir(exist_ok=True)
    today = datetime.now().strftime("%Y%m%d")
    action_needed = 0

    with sync_playwright() as pw:
        context = pw.chromium.launch_persistent_context(
            str(profile), channel="chrome", headless=not windowed,
            viewport={"width": 1400, "height": 900},
            args=STEALTH_ARGS,
        )
        context.add_init_script(STEALTH_JS + INIT_JS)
        page = (list(context.pages) or [context.new_page()])[0]

        for url in targets:
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(5000)
                # Nudge the page so newest content is loaded.
                page.mouse.wheel(0, 1500)
                page.wait_for_timeout(1500)
            except Exception as error:
                log("ERROR loading " + url + " (" + str(error) + ")")
                action_needed += 1
                continue

            if looks_logged_out(page):
                log("ACTION NEEDED: session expired or login wall at " + url
                    + " — run: python3 scrape.py \"" + url + "\" and log in once")
                action_needed += 1
                continue

            try:
                title = page.title()
                text = read_text(page)
                if not text or len(text.strip()) < 40:
                    log("WARNING: page nearly empty at " + url
                        + " — not saved (probably still loading)")
                    action_needed += 1
                    continue
                fixed = "auto_" + today + "_" + slugify(title)
                save(page, page.url, title, text, fixed_name=fixed)
            except Exception as error:
                log("ERROR capturing " + url + " (" + str(error) + ")")
                action_needed += 1

        try:
            context.close()
        except Exception:
            pass

    if action_needed:
        log("Auto refresh finished with " + str(action_needed)
            + " item(s) needing attention.")
    else:
        log("Auto refresh finished clean.")
    return action_needed


# ------------------------------------------------------------------ selftest

def selftest():
    MATERIALS.mkdir(exist_ok=True)
    before = set(MATERIALS.glob("*.md"))
    data_url = ("data:text/html,<title>mentor-selftest</title>"
                "<p>capture selftest content - the mentor page capturer "
                "reads page text and stores it for the studying AI. "
                "This sentence pads the body so the non-empty check passes."
                "</p>")

    with sync_playwright() as pw:
        context = pw.chromium.launch_persistent_context(
            str(TEST_PROFILE), headless=True,
            viewport={"width": 1200, "height": 800},
        )
        context.add_init_script(INIT_JS)
        page = list(context.pages)[0]
        page.goto(data_url, wait_until="domcontentloaded")
        page.wait_for_timeout(600)

        has_button = page.evaluate(
            "!!document.getElementById('mentor-capture-host')")
        print(("PASS" if has_button else "FAIL") + ": capture button injected")

        page.evaluate("window.__mentorWant = Date.now()")
        deadline = time.time() + 5
        saved = None
        seen = {}
        while time.time() < deadline:
            pump(context, seen)
            time.sleep(0.2)
            fresh = set(MATERIALS.glob("*.md")) - before
            if fresh:
                saved = fresh.pop()
                break

        ok_text = saved is not None and "capture selftest content" in saved.read_text(
            encoding="utf-8")
        print(("PASS" if ok_text else "FAIL") + ": click flag -> file saved with text")

        png_ok = saved is not None and saved.with_suffix(".png").exists()
        print(("PASS" if png_ok else "FAIL") + ": full-page screenshot saved")
        if saved:
            saved.unlink(missing_ok=True)
            saved.with_suffix(".png").unlink(missing_ok=True)
        context.close()

    # Auto-mode mechanics on a data URL with the test profile.
    before2 = set(MATERIALS.glob("auto_*.md"))
    run_auto([data_url], TEST_PROFILE)
    fresh_auto = set(MATERIALS.glob("auto_*.md")) - before2
    ok_auto = any("capture selftest content" in path.read_text(encoding="utf-8")
                  for path in fresh_auto)
    print(("PASS" if ok_auto else "FAIL") + ": auto mode saves without clicks")

    for path in fresh_auto:
        path.unlink()
        path.with_suffix(".png").unlink(missing_ok=True)

    return has_button and ok_text and png_ok and ok_auto


if __name__ == "__main__":
    args = sys.argv[1:]

    def flag(name):
        return name in args

    def value(name, default):
        if name in args:
            return args[args.index(name) + 1]
        return default

    if flag("--selftest"):
        sys.exit(0 if selftest() else 1)

    profile = Path(value("--profile", str(PROFILE)))

    if flag("--auto"):
        targets_file = Path(value("--targets", str(DEFAULT_TARGETS)))
        if not targets_file.exists():
            print("missing targets file:", targets_file)
            sys.exit(2)
        targets = [line.strip() for line in targets_file.read_text().splitlines()
                   if line.strip() and not line.strip().startswith("#")]
        sys.exit(0 if run_auto(targets, profile,
                               windowed=flag("--windowed")) == 0 else 3)

    targets = [argument for argument in args if not argument.startswith("--")]
    if not targets:
        print(__doc__)
        sys.exit(2)
    run_interactive(targets, profile)
