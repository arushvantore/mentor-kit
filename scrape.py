#!/usr/bin/env python3
"""Mentor background tracker v4 — full portal coverage, zero user effort.

SAFETY: read-only. Never types, never submits, never starts tests, never
uploads off this Mac. Credentials live in .browser-profile/ only.

WHAT THE AI SEES (all in materials/):
  live_<page>.md          current state of every portal/Slack page
  archive_YYYYMMDD_<page> daily history (past activity)
  questions/live_<q>.md   full text of every assignment question
                           (clicked open automatically, then closed)
  captures.log            timeline + ACTION NEEDED alerts

PAGES COVERED:
  HOT (every --interval sec, default 120):
      dashboard, all assignments, all quizzes, question of the day, Slack
  DEEP (every --deep-every hot cycles, default 10 => ~20 min):
      every subject x every tab (Overview/Lectures/Assignments/Quiz/
      Contest) for all course ids in subjects.txt, hub extras (Calendar,
      My Timeline, Expert Sessions, Requests, Leaderboard), plus every
      cool target + auto-discovered link in targets.txt
      assignment/quiz rows are CLICKED OPEN on lists (question text /
      test info read from the opened tab, then closed)

MODES:
  scrape.py --watch [--interval N] [--deep-every M]   background daemon
  scrape.py --auto [--hot]           one full cycle (--hot = hot only)
  scrape.py <url> ...                LOGIN WINDOW (visible, no button)
  scrape.py --selftest               offline end-to-end check
"""

import json
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE = Path(__file__).resolve().parent
MATERIALS = BASE / "materials"
QUESTIONS = MATERIALS / "questions"
PROFILE = BASE / ".browser-profile"
TEST_PROFILE = BASE / ".browser-profile-test"
LOGF = BASE / "captures.log"
HOT_TARGETS = BASE / "targets-hot.txt"
COOL_TARGETS = BASE / "targets.txt"
SUBJECTS_FILE = BASE / "subjects.txt"
QSTATE = QUESTIONS / "state.json"

LOGIN_HINTS = ("signin", "login", "sso", "authorize", "oauth", "auth")
ALLOWED_HOSTS = ("my.newtonschool.co", "app.slack.com")
FORBIDDEN = ("logout", "signout", "sign-out", "delete-account", "unregister",
             "/user/", "apply_form", "privacy-policy", "terms-and-conditions",
             "force-cold-boot")
ERROR_TEXTS = ("Couldn\u2019t load this page", "Couldn't load this page",
               "Page Not Found", "404")
SUBTABS = ("Overview", "Lectures", "Assignments", "Quiz", "Contest")
OPENABLE = ("subTab=Assignments", "subTab=Quiz", "subTab=Contest",
            "all_assignments", "all_assessments")
HUB = "tjj12ybxo9tt"
MAX_OPENS_PER_CYCLE = 70
Q_FRESH_DAYS = 1

STEALTH_ARGS = [
    "--disable-blink-features=AutomationControlled",
    "--no-first-run",
    "--no-default-browser-check",
]
STEALTH_JS = """
Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
"""

LINK_JS = """
() => Array.from(document.querySelectorAll('a[href]'))
  .map(a => ((a.innerText || a.getAttribute('aria-label') || '').trim()
             .replace(/\\s+/g, ' ').slice(0, 70)) + ' :: ' + a.href)
  .filter(s => s.includes(':: http'))
  .slice(0, 150)
"""


def log(message):
    line = datetime.now().isoformat(timespec="seconds") + " " + message
    print(line, flush=True)
    with LOGF.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def slugify(text, limit=60):
    slug = re.sub(r"[^a-z0-9]+", "-", (text or "page").lower()).strip("-")
    return slug[:limit] or "page"


def url_slug(url):
    # keep the query string: tabs are distinguished only by query params
    return slugify(url.split("#", 1)[0], limit=120)


def read_text(page):
    return page.evaluate("() => (document.body ? document.body.innerText : '')")


def read_links(page):
    try:
        return page.evaluate(LINK_JS) or []
    except Exception:
        return []


def looks_logged_out(page):
    try:
        if page.locator("input[type=password]").count() > 0:
            return True
        lower = page.url.lower()
        return any(hint in lower for hint in LOGIN_HINTS)
    except Exception:
        return False


def save(page, slug, text, links, subdir=None, archive=True):
    now = datetime.now()
    title = page.title()
    header = ("# " + str(title) + "\n\nURL: " + str(page.url)
              + "\nCaptured: " + now.isoformat(timespec="seconds") + "\n\n---\n\n")
    body = text or ""
    if any(err in body for err in ERROR_TEXTS):
        body = ("(Portal showed an error / empty page here — this feature "
                "is probably unavailable for this view.)\n")
    footer = ""
    if links:
        footer = "\n\n## Links on this page\n" + "".join(
            "- " + item + "\n" for item in links)

    outdir = subdir or MATERIALS
    outdir.mkdir(parents=True, exist_ok=True)
    names = ["live_" + slug]
    if archive:
        names.append("archive_" + now.strftime("%Y%m%d") + "_" + slug)

    saved = []
    for stem in names:
        md_path = outdir / (stem + ".md")
        md_path.write_text(header + body + footer + "\n", encoding="utf-8")
        try:
            page.screenshot(path=str(md_path.with_suffix(".png")), full_page=True)
        except Exception as error:
            log("  screenshot skipped: " + str(error))
        saved.append(md_path.name)
    log("SAVED " + " + ".join(saved) + "  <- " + str(page.url))


def capture_target(page, url):
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(4500)
        for _ in range(3):
            page.mouse.wheel(0, -1400)
            page.wait_for_timeout(250)
        page.wait_for_timeout(600)
    except Exception as error:
        log("ERROR loading " + url + " (" + str(error) + ")")
        return []

    if looks_logged_out(page):
        log("ACTION NEEDED: session expired or login wall at " + url
            + " — stop the daemon and run a login window (see MENTOR.md §6)")
        return []

    try:
        text = read_text(page)
        links = read_links(page)
        if not text or len(text.strip()) < 40:
            log("NO CONTENT (blank page): " + url)
            return links
        # slug from the REQUESTED url: subject context lives in the request
        # (the portal redirects all subject tabs to the hub URL, which would
        # otherwise make every subject overwrite the same file)
        save(page, url_slug(url), text, links)
        note_attendance(url, text)
        return links
    except Exception as error:
        log("ERROR capturing " + url + " (" + str(error) + ")")
        return []


def note_attendance(url, text):
    """Lectures pages show the authoritative 'N/M Attended' summary."""
    try:
        if "subTab=Lectures" not in url or "subject=" not in url:
            return
        match = re.search(r"(\d+)\s*/\s*(\d+)\s*Attended", text)
        if not match:
            return
        sid = url.split("subject=")[1].split("&")[0]
        API_DIR.mkdir(parents=True, exist_ok=True)
        state_file = API_DIR / "attendance.json"
        state = {}
        if state_file.exists():
            state = json.loads(state_file.read_text(encoding="utf-8"))
        state[sid] = {"attended": int(match.group(1)),
                      "total": int(match.group(2))}
        state_file.write_text(json.dumps(state, indent=1),
                              encoding="utf-8")
    except Exception:
        pass


# ---------- question opening (click rows, read new tab, close) ----------

def load_qstate():
    try:
        return json.loads(QSTATE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_qstate(state):
    QUESTIONS.mkdir(parents=True, exist_ok=True)
    QSTATE.write_text(json.dumps(state, indent=1), encoding="utf-8")


def q_fresh(state, key):
    entry = state.get(key)
    if not entry:
        return False
    try:
        seen = datetime.fromisoformat(entry["seen"])
        return datetime.now() - seen < timedelta(days=Q_FRESH_DAYS)
    except Exception:
        return False


ROW_JS = """
() => {
  const out = [];
  const seen = new Set();
  document.querySelectorAll('div,td,span,a').forEach(el => {
    const st = getComputedStyle(el);
    if (st.cursor !== 'pointer') return;
    const t = (el.innerText || '').trim().replace(/\\s+/g, ' ');
    if (t.length < 15 || t.length > 480) return;
    if (seen.has(t)) return;
    const isRowish = /\\b(easy|medium|hard)\\b/i.test(t)
      || /\\b\\d{1,2}\\s+[A-Z]{3}\\s+\\d{4}\\b/.test(t)
      || /\\b0\\/\\d+\\b/.test(t);
    if (!isRowish) return;
    // skip lone date / score fragments (they collide across rows)
    if (/^[\\d\\sA-Z]{6,15}$/.test(t) && /\\d{1,2}\\s+[A-Z]{3}\\s+\\d{4}/.test(t)
        && t.split(' ').length <= 4) return;
    if (/^\\s*0?\\/\\d+\\s*$/.test(t)) return;
    seen.add(t);
    out.push(t);
  });
  return out.slice(0, 250);
}
"""


def title_from_row(row):
    return row.strip()[:85]


def open_questions(page, list_url, state, budget):
    """Open each uncached assignment/quiz row, read it, close it."""
    opened = 0
    try:
        if page.url.split("?")[0] != list_url.split("?")[0]:
            page.goto(list_url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(4500)
        seen_rows = -1
        for _ in range(24):
            page.mouse.wheel(0, 2200)
            page.wait_for_timeout(300)
            if _ % 4 == 3:
                rows_now = page.evaluate(ROW_JS)
                if len(rows_now) == seen_rows:
                    break
                seen_rows = len(rows_now)
        rows = page.evaluate(ROW_JS)
    except Exception as error:
        log("  open_questions scan failed: " + str(error))
        return 0

    for row in rows:
        if opened >= budget:
            break
        title = title_from_row(row)
        if not title:
            continue
        key = slugify(title, 70)
        if q_fresh(state, key):
            continue
        try:
            found = page.evaluate("""(t) => {
              const c = Array.from(document.querySelectorAll('div,span,a,td'))
                .filter(el => { const st = getComputedStyle(el);
                  return st.cursor === 'pointer'
                    && (el.innerText || '').trim().replace(/\\s+/g, ' ') === t; });
              if (!c.length) return false;
              c[c.length - 1].setAttribute('data-probe', '1');
              return true;
            }""", row if len(row) < 480 else title)
            if not found:
                found = page.evaluate("""(t) => {
                  const c = Array.from(document.querySelectorAll('div,span,a,td'))
                    .filter(el => { const st = getComputedStyle(el);
                      const v = (el.innerText || '').trim().replace(/\\s+/g, ' ');
                      return st.cursor === 'pointer' && v.length < 85
                        && v.indexOf(t) === 0; });
                  if (!c.length) return false;
                  c[c.length - 1].setAttribute('data-probe', '1');
                  return true;
                }""", title)
            if not found:
                # contest/list rows: title lives in its own small div
                lead = re.split(r"\s+(?=easy\b|medium\b|hard\b)", title,
                                maxsplit=1, flags=re.IGNORECASE)[0].strip()
                found = page.evaluate("""(t) => {
                  const c = Array.from(document.querySelectorAll('div,span,a,td'))
                    .filter(el => { const st = getComputedStyle(el);
                      const v = (el.innerText || '').trim().replace(/\\s+/g, ' ');
                      return st.cursor === 'pointer' && v === t; });
                  if (!c.length) return false;
                  c[c.length - 1].setAttribute('data-probe', '1');
                  return true;
                }""", lead)
            if not found:
                continue
            before = len(page.context.pages)
            page.click('[data-probe="1"]', timeout=6000)
            page.wait_for_timeout(3500)
            pages = page.context.pages

            if len(pages) > before:
                detail = pages[-1]
                try:
                    detail.wait_for_timeout(1500)
                    text = detail.read_text() if False else detail.evaluate(
                        "() => document.body.innerText")
                    durl = detail.url
                    save_detail(durl, title, text)
                    state[key] = {"seen": datetime.now().isoformat(
                        timespec="seconds"), "url": durl}
                    opened += 1
                finally:
                    try:
                        detail.close()
                    except Exception:
                        pass
            elif page.url.split("?")[0] != list_url.split("?")[0]:
                text = read_text(page)
                save_detail(page.url, title, text)
                state[key] = {"seen": datetime.now().isoformat(
                    timespec="seconds"), "url": page.url}
                opened += 1
                page.go_back(wait_until="domcontentloaded", timeout=30000)
                page.wait_for_timeout(2500)
            else:
                state[key] = {"seen": datetime.now().isoformat(
                    timespec="seconds"), "url": list_url, "noopen": True}
            page.evaluate(
                "() => document.querySelectorAll('[data-probe]')"
                ".forEach(e => e.removeAttribute('data-probe'))")
        except Exception as error:
            log("  row open failed (" + str(error)[:70] + "): "
                + title[:50])
            try:
                page.keyboard.press("Escape")
                page.wait_for_timeout(500)
            except Exception:
                pass
            state.setdefault(key, {"seen": datetime.now().isoformat(
                timespec="seconds"), "url": list_url, "error": True})
    if opened:
        log("OPENED " + str(opened) + " question(s) from " + list_url)
    return opened


def save_detail(durl, title, text):
    now = datetime.now()
    header = ("# " + title + "\n\nURL: " + durl
              + "\nCaptured: " + now.isoformat(timespec="seconds")
              + "\nOpened automatically by the tracker (read-only).\n\n---\n\n")
    slug = url_slug(durl)
    for stem in ("live_" + slug,
                 "archive_" + now.strftime("%Y%m%d") + "_" + slug):
        path = QUESTIONS / (stem + ".md")
        path.write_text(header + (text or "") + "\n", encoding="utf-8")
    log("SAVED question " + title[:60] + " -> " + durl)


API_DIR = MATERIALS / "api"


def make_api_collector():
    data = {"assignments": {}, "assessments": {}, "lectures": {}, "perf": {}}

    def on_response(resp):
        try:
            if resp.status != 200 or "json" not in resp.headers.get(
                    "content-type", ""):
                return
            url = resp.url
            if "/api/v2/course/" not in url:
                return
            body = resp.text()
            if "/assignment/all/" in url:
                for item in json.loads(body).get("results", []):
                    data["assignments"][item.get("hash")] = item
            elif "/assessment/all/" in url:
                for item in json.loads(body).get("results", []):
                    data["assessments"][item.get("hash")] = item
            elif "/lecture/all/" in url:
                sid = url.split("/course/h/")[1].split("/")[0]
                payload = json.loads(body)
                if isinstance(payload.get("data"), dict):
                    payload = payload["data"]
                bucket = data["lectures"].setdefault(sid, {})
                for item in payload.get("results", []):
                    bucket[item.get("hash")] = item
            elif "/self_performance/" in url:
                sid = url.split("/course/h/")[1].split("/")[0]
                payload = json.loads(body)
                if isinstance(payload.get("data"), dict):
                    payload = payload["data"]
                data["perf"][sid] = payload
        except Exception:
            pass

    return data, on_response


def write_digest(data):
    if not (data["assignments"] or data["assessments"] or data["perf"]):
        return
    API_DIR.mkdir(parents=True, exist_ok=True)
    state_file = API_DIR / "digest.json"
    prior = {}
    if state_file.exists():
        try:
            prior = json.loads(state_file.read_text(encoding="utf-8"))
        except Exception:
            prior = {}

    def merge(new_items, old_items):
        merged = dict(old_items or {})
        for key, value in (new_items or {}).items():
            if value:
                merged[key] = value
        return merged

    merged_perf = dict(prior.get("perf") or {})
    for sid, perf in (data["perf"] or {}).items():
        base = merged_perf.get(sid) or {}
        if perf:
            base.update({k: v for k, v in perf.items() if v is not None})
        merged_perf[sid] = base

    state = {
        "assignments": merge(data["assignments"], prior.get("assignments")),
        "assessments": merge(data["assessments"], prior.get("assessments")),
        "perf": merged_perf,
    }
    for sid, bucket in (data["lectures"] or {}).items():
        state.setdefault("lectures", {})[sid] = merge(
            bucket, (prior.get("lectures") or {}).get(sid))
    state.setdefault("lectures", prior.get("lectures") or {})
    state_file.write_text(json.dumps(state, indent=1), encoding="utf-8")
    data = state

    now = datetime.now()
    def by_subject(items):
        groups = {}
        for item in items.values():
            course = item.get("course") or {}
            key = (course.get("short_display_name")
                   or course.get("hash") or "unknown")
            groups.setdefault(key, []).append(item)
        return groups

    out = ["# Portal API digest (auto-collected, read-only)",
           "Captured: " + now.isoformat(timespec="seconds"),
           "Source: the portal's own XHR responses observed while pages load.",
           "", "## Attendance (self_performance)"]

    def when(ms):
        if ms in (None, "", "None"):
            return "-"
        try:
            return datetime.fromtimestamp(
                int(str(ms)) / 1000).strftime("%Y-%m-%d %H:%M")
        except Exception:
            return str(ms)[:16]

    def lecture_attend(sid):
        bucket = data["lectures"].get(sid) or {}
        if not bucket:
            return None
        attended = sum(1 for lec in bucket.values() if lec.get("attended"))
        return str(attended) + "/" + str(len(bucket)) + " (partial)"

    page_attend = {}
    attend_file = API_DIR / "attendance.json"
    if attend_file.exists():
        try:
            page_attend = json.loads(attend_file.read_text(encoding="utf-8"))
        except Exception:
            page_attend = {}

    all_sids = sorted(set(list(data["perf"]) + list(data["lectures"])
                          + list(page_attend)))
    for sid in all_sids:
        if sid in page_attend:
            entry = page_attend[sid]
            out.append("- " + sid + ": attended "
                       + str(entry.get("attended")) + "/"
                       + str(entry.get("total")) + " (Lectures page)")
            continue
        perf = data["perf"].get(sid, {})
        total = perf.get("total_lectures_attended")
        count = perf.get("total_lectures")
        if total is None or count is None:
            fallback = lecture_attend(sid)
            if fallback:
                out.append("- " + sid + ": attended " + fallback)
            else:
                out.append("- " + sid + ": n/a (see Lectures capture)")
        else:
            out.append("- " + sid + ": attended " + str(total) + "/"
                       + str(count))

    for subject, items in sorted(by_subject(data["assignments"]).items()):
        out.append("")
        out.append("## Assignments — " + subject)
        for a in sorted(items, key=lambda x: str(x.get("end_timestamp"))):
            qs = a.get("assignment_questions") or []
            solved = sum(1 for q in qs
                         if (q.get("earned_points") or 0) > 0)
            out.append("- " + str(a.get("title")) + " | questions "
                       + str(solved) + "/" + str(len(qs)) + " | due "
                       + when(a.get("end_timestamp")))
            for q in qs:
                out.append("    - " + str(q.get("question_title"))
                           + " | xp " + str(q.get("earned_points")) + "/"
                           + str(q.get("earnable_points"))
                           + " | deadline " + when(q.get("deadline")))

    for subject, items in sorted(by_subject(data["assessments"]).items()):
        out.append("")
        out.append("## Quizzes — " + subject)
        for a in sorted(items, key=lambda x: str(x.get("start_timestamp"))):
            xp = a.get("earnable_xp") or {}
            out.append("- " + str(a.get("title"))
                       + " | " + when(a.get("start_timestamp"))
                       + " -> " + when(a.get("end_timestamp"))
                       + " | xp " + str(xp.get("earned_points")) + "/"
                       + str(xp.get("earnable_points"))
                       + " | topics " + ", ".join(a.get("topics") or []))

    for sid, lectures in sorted(data["lectures"].items()):
        out.append("")
        out.append("## Lectures observed — " + sid)
        attended = sum(1 for l in lectures.values() if l.get("attended"))
        watched = sum(1 for l in lectures.values() if l.get("watched"))
        out.append("- " + str(len(lectures)) + " lectures | attended "
                   + str(attended) + " | watched " + str(watched))
        for lec in sorted(lectures.values(),
                          key=lambda x: str(x.get("start_timestamp"))):
            out.append("    - " + str(lec.get("title"))[:80]
                       + " | " + when(lec.get("start_timestamp"))
                       + " | attended=" + str(lec.get("attended"))
                       + " watched=" + str(lec.get("watched")))

    text = "\n".join(out) + "\n"
    (API_DIR / "digest.md").write_text(text, encoding="utf-8")
    (API_DIR / ("archive_" + now.strftime("%Y%m%d") + "_digest.md")
     ).write_text(text, encoding="utf-8")
    log("SAVED api/digest.md (assignments "
        + str(len(data["assignments"])) + ", quizzes "
        + str(len(data["assessments"])) + ", subjects w/ attendance "
        + str(len(data["perf"])) + ")")


# ---------- harvest what's below each lecture video ----------

LECTQ_DIR = MATERIALS / "lecture-questions"
LECTQ_STATE = LECTQ_DIR / "state.json"
UNSAFE_CLICK = re.compile(r"attempt|start|submit|complete|resume|save|"
                          r"register|pay|buy", re.IGNORECASE)


def _load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception:
        return {}


def _click_label(page, label):
    """Click a UI label ONLY if it is read-only (never attempt/start/
    submit/complete...). Matches exact text or text + count badge."""
    if UNSAFE_CLICK.search(label):
        return False
    try:
        found = page.evaluate("""(t) => {
          const c = Array.from(document.querySelectorAll(
              'div,span,a,button,td'))
            .filter(el => {
              if (getComputedStyle(el).cursor !== 'pointer') return false;
              const v = (el.innerText || '').trim().replace(/\\s+/g, ' ');
              return v === t || (v.startsWith(t + ' ')
                && /^[\\d\\s]+$/.test(v.slice(t.length + 1)));
            });
          if (!c.length) return false;
          c[c.length - 1].setAttribute('data-probe', '1');
          return true;
        }""", label)
        if not found:
            return False
        page.click('[data-probe="1"]', timeout=5000)
        page.wait_for_timeout(3000)
        page.evaluate("""() => document.querySelectorAll('[data-probe]')
            .forEach(e => e.removeAttribute('data-probe'))""")
        return True
    except Exception:
        return False


def _expand_read_more(page):
    for _ in range(14):
        try:
            loc = page.get_by_text("Read More", exact=True)
            if loc.count() == 0:
                break
            loc.nth(0).click(timeout=2500)
            page.wait_for_timeout(500)
        except Exception:
            break


def _walk_quiz(page, quiz_block):
    """Quizzes show one question at a time with Previous/Next — walk
    BOTH directions (read-only, safe) until QUESTION 1..total are all
    captured (the portal can open a quiz mid-way, e.g. at 6/10)."""
    fails = 0
    for _attempt in range(60):
        found = re.findall(r"QUESTION\s*(\d+)/(\d+)", quiz_block)
        if not found:
            break
        seen = {int(a) for a, _b in found}
        total = max(int(b) for _a, b in found)
        if seen >= set(range(1, total + 1)):
            break
        label = ("Next" if max(seen) < total
                 else "Previous" if min(seen) > 1 else None)
        if label is None:
            break
        if not _click_label(page, label):
            other = "Previous" if label == "Next" else "Next"
            if not _click_label(page, other):
                fails += 1
                if fails >= 3:
                    break
                continue
        nxt = read_text(page)
        new_chunks = []
        for marker in re.finditer(r"QUESTION\s*(\d+)/(\d+)", nxt):
            k = int(marker.group(1))
            if k in seen:
                continue
            start = marker.start()
            end = nxt.find("Copyright", start)
            new_chunks.append(nxt[start:end] if end > start
                              else nxt[start:start + 4000])
        if not new_chunks:
            # stepping through already-seen questions (e.g. 10 -> 9 -> ...)
            # is normal before reaching an unseen one — keep going a while
            fails += 1
            if fails > total:
                break
            continue
        fails = 0
        quiz_block += ("\n" + "\n").join(new_chunks)
    return quiz_block


def harvest_lectures(page, sid, state, budget):
    """Visit lectures of subject sid; save EVERYTHING under the video:
    in-class quiz questions (Revise view only — never Attempt/Start),
    post-class / in-class assignment question text, quiz cards.
    Returns number of lectures visited."""
    hashes = []
    try:
        digest = json.loads((API_DIR / "digest.json").read_text(
            encoding="utf-8"))
        for item in (digest.get("lectures", {}).get(sid) or {}).values():
            if item.get("hash"):
                hashes.append(item["hash"])
    except Exception:
        pass
    for key in state:
        if key.startswith(sid + "_"):
            hashes.append(key.split("_", 1)[1])
    hashes = list(dict.fromkeys(hashes))
    if not hashes:
        log("  lecture harvest: no hashes known for " + sid)
        return 0
    visited = 0
    i = 0
    while i < len(hashes) and visited < budget:
        lec_hash = hashes[i]
        i += 1
        key = sid + "_" + lec_hash
        entry = state.get(key)
        if entry and entry.get("seen"):
            try:
                if datetime.now() - datetime.fromisoformat(
                        entry["seen"]) < timedelta(hours=24):
                    continue
            except Exception:
                pass
        url = ("https://my.newtonschool.co/course/" + sid + "/lecture/"
               + lec_hash + "?lectureTab=assignment")
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(4500)
        except Exception as error:
            log("  lecture load failed: " + str(error)[:70])
            continue
        if looks_logged_out(page):
            log("ACTION NEEDED: session expired at " + url
                + " — stop the daemon and run a login window (MENTOR.md §6)")
            break
        visited += 1
        # grow the lecture list from the Course Content sidebar
        title = ""
        try:
            anchors = page.evaluate(
                "() => Array.from(document.querySelectorAll('a'))"
                ".map(a => a.getAttribute('href')||'')")
            for href in anchors:
                m = re.match(r"/course/" + re.escape(sid)
                             + r"/lecture/([a-z0-9]+)(.*)", href)
                if not m:
                    continue
                if m.group(1) not in hashes:
                    hashes.append(m.group(1))
                if m.group(1) == lec_hash and m.group(2):
                    label = page.evaluate(
                        """(h) => { const a = Array.from(
                            document.querySelectorAll('a')).find(
                            x => (x.getAttribute('href')||'').indexOf(h) === 0);
                            return a ? (a.innerText||'') : ''; }""",
                        "/lecture/" + lec_hash)
                    title = label.split("\n")[0].strip()[:120]
        except Exception:
            pass
        text = read_text(page)
        start = text.find("Assignments")
        end = text.find("Copyright", start if start >= 0 else 0)
        block = (text[start:end] if start >= 0 and end > start
                 else text[start:] if start >= 0 else "")
        _expand_read_more(page)
        text2 = read_text(page)
        start2 = text2.find("Assignments")
        end2 = text2.find("Copyright", start2 if start2 >= 0 else 0)
        if start2 >= 0 and len(text2[start2:end2] if end2 > start2
                              else text2[start2:]) > len(block):
            block = (text2[start2:end2] if end2 > start2
                     else text2[start2:])
        quiz_block = ""
        if "In-class Quizzes" in text2:
            if _click_label(page, "In-class Quizzes"):
                qtext = read_text(page)
                qstart = qtext.find("In-class Quizzes")
                qend = qtext.find("Copyright", qstart if qstart >= 0 else 0)
                quiz_block = (qtext[qstart:qend] if qstart >= 0 and qend > 0
                              else qtext[qstart:] if qstart >= 0
                              else qtext[-3000:])
                # one question at a time -> walk Next through all of them
                quiz_block = _walk_quiz(page, quiz_block)
                # read-only "Revise"/"View Solutions" shows questions +
                # explanations when they aren't already on the page
                if "QUESTION" not in quiz_block:
                    label = None
                    if "Revise" in quiz_block:
                        label = "Revise"
                    elif "View Solutions" in quiz_block:
                        label = "View Solutions"
                    if label and _click_label(page, label):
                        page.wait_for_timeout(1500)
                        rtext = read_text(page)
                        rpos = -1
                        for marker in ("QUESTION 1/", "QUESTION1/",
                                       "Explanation:", "Classroom Quiz -"):
                            rpos = rtext.find(marker)
                            if rpos >= 0:
                                break
                        if rpos >= 0:
                            rend = rtext.find("Copyright", rpos)
                            piece = (rtext[rpos:rend] if rend > rpos
                                     else rtext[rpos:])
                            if "QUESTION" in piece or "Explanation" in piece:
                                quiz_block += ("\n\n=== Revise view ("
                                               "questions) ===\n" + piece)
                                quiz_block = _walk_quiz(page, quiz_block)
        has_q = ("Q1." in block or "QUESTION 1" in quiz_block
                 or "QUESTION 1/1" in quiz_block
                 or "Classroom Quiz" in quiz_block)
        LECTQ_DIR.mkdir(exist_ok=True)
        body = ("# " + (title or lec_hash) + "  [" + sid + "]\n"
                "URL: " + url + "\n"
                "Captured: " + datetime.now().isoformat(timespec="seconds")
                + " by lecture harvester (read-only).\n\n---\n\n"
                "=== Assignments tab (quiz cards + in-class + "
                "post-class sections) ===\n" + block.strip() + "\n")
        if quiz_block.strip():
            body += ("\n=== In-class Quizzes tab ===\n"
                     + quiz_block.strip() + "\n")
        if not has_q:
            body += "\n(no questions below this lecture at capture time)\n"
        (LECTQ_DIR / (key + ".md")).write_text(body, encoding="utf-8")
        state[key] = {"seen": datetime.now().isoformat(timespec="seconds"),
                      "title": title, "questions": bool(has_q)}
    return visited


def _norm_text(value):
    return re.sub(r"[^a-z0-9]", "", str(value).lower())


def _matched_subjects(name):
    needle = _norm_text(name)
    out = []
    for line in read_lines(SUBJECTS_FILE):
        parts = line.split("|")
        if len(parts) != 2:
            continue
        sid_norm = _norm_text(parts[0])
        label_norm = _norm_text(parts[1])
        if needle and (needle == sid_norm or needle in label_norm
                       or label_norm in needle):
            out.append((parts[0].strip(), parts[1].strip()))
    return out


# ---------- export: every question of one subject, one file ----------

def export_subject(name):
    """--export <subject>: one file with EVERY question of that subject
    (in-class, post-class, solved, due) + full texts already captured."""
    if not (API_DIR / "digest.json").exists():
        print("No digest yet — run ./refresh.sh first.")
        return 1
    state = json.loads((API_DIR / "digest.json").read_text(encoding="utf-8"))
    needle = name.strip().lower()
    matched = _matched_subjects(name)
    label = matched[0][1] if len(matched) == 1 else name.strip()
    matched_sids = [m[0] for m in matched] or []

    def is_this(item):
        course = item.get("course") or {}
        hay = (str(course.get("short_display_name")) + " "
               + str(course.get("name"))).lower()
        return needle in hay or label.lower() in hay

    assignments = [a for a in state.get("assignments", {}).values()
                   if is_this(a)]
    quizzes = [a for a in state.get("assessments", {}).values()
               if is_this(a)]
    if not assignments and not quizzes:
        print("No data found for '" + name + "'. Known subjects:")
        for line in read_lines(SUBJECTS_FILE):
            print("  " + line)
        return 1

    texts = {}
    for path in sorted(QUESTIONS.glob("live_*.md")):
        try:
            raw = path.read_text(encoding="utf-8")
        except Exception:
            continue
        if not raw.startswith("# "):
            continue
        header = raw.splitlines()[0][2:]
        url = ""
        for line in raw.splitlines()[1:6]:
            if line.startswith("URL:"):
                url = line.split("URL:", 1)[1].strip()
        body = raw.split("\n---\n", 1)
        body = body[1] if len(body) == 2 else raw
        cut = body.find("Generated Expected Output")
        if cut > 0:
            body = body[:cut]
        texts.setdefault(header, (url, body.strip()))

    def find_text(qtitle):
        for header, value in texts.items():
            if header.startswith(qtitle):
                return value
        return None

    def when(value):
        if value in (None, "", "None"):
            return "?"
        text = str(value)
        try:
            if "T" in text:
                return datetime.fromisoformat(
                    text.replace("Z", "+00:00")).astimezone().strftime(
                        "%Y-%m-%d %H:%M")
            return datetime.fromtimestamp(
                int(text) / 1000).strftime("%Y-%m-%d %H:%M")
        except Exception:
            return text[:16]

    status_map = {3: "SOLVED", 1: "PARTIAL", 2: "NOT SOLVED"}
    lines = ["# EVERY " + label + " question (portal, till now)",
             "Generated: " + datetime.now().isoformat(timespec="seconds")
             + " by `scrape.py --export " + name + "`",
             "",
             "For the AI tutor: teach these in due-date order. Status and",
             "XP are the student's real portal state. Question text is",
             "included in a code block wherever the tracker captured it;",
             "questions without text are listed at the end.",
             ""]
    total_q = 0
    solved_q = 0
    no_text = []
    assignments.sort(key=lambda a: str(a.get("end_timestamp")))
    for a in assignments:
        title = str(a.get("title"))
        kind = "Post Class" if "Post Class" in title else (
            "In Class" if "In Class" in title else (
                "Contest" if "Contest" in title else "Other"))
        title_clean = title.replace(" - Post Class", ""
                                    ).replace(" - In Class", "")
        questions = a.get("assignment_questions") or []
        total_q += len(questions)
        lines.append("---")
        lines.append("## " + title_clean + "  [" + kind + "]  — due "
                     + when(a.get("end_timestamp")))
        for q in questions:
            qtitle = str(q.get("question_title"))
            status = status_map.get(q.get("attempt_status"), "UNKNOWN")
            if q.get("earned_points", 0) >= (q.get("earnable_points")
                                             or 0) and q.get(
                                                 "earnable_points"):
                status = "SOLVED"
            if status == "SOLVED":
                solved_q += 1
            lines.append("")
            lines.append("### " + qtitle + " — " + str(
                q.get("earned_points")) + "/" + str(
                q.get("earnable_points")) + " XP — " + status
                + " — deadline " + when(q.get("deadline")))
            if q.get("topics"):
                lines.append("Topics: " + ", ".join(q["topics"]))
            found = find_text(qtitle)
            if found:
                url, body = found
                lines.append("")
                if url:
                    lines.append("URL: " + url)
                lines.append("")
                lines.append("```")
                lines.append(body)
                lines.append("```")
            else:
                no_text.append(qtitle)
                lines.append("(full text not captured yet — tracker will "
                             "open this row on its next sweep)")

    if quizzes:
        lines.append("")
        lines.append("---")
        lines.append("## Quizzes / quiz contests (" + str(len(quizzes))
                     + ") — schedules only")
        lines.append("(Portal shows quiz QUESTIONS only after starting a "
                     "test — starting tests is forbidden, so no question "
                     "text exists for these.)")
        for quiz in sorted(quizzes, key=lambda x: str(x.get(
                "start_timestamp"))):
            xp = quiz.get("earnable_xp") or {}
            lines.append("- " + str(quiz.get("title")) + " — "
                         + when(quiz.get("start_timestamp")) + " -> "
                         + when(quiz.get("end_timestamp")) + " — xp "
                         + str(xp.get("earned_points")) + "/"
                         + str(xp.get("earnable_points")))

    lecture_files = []
    for sid in matched_sids:
        lecture_files.extend(sorted(LECTQ_DIR.glob(sid + "_*.md")))
    with_questions = 0
    if lecture_files:
        lines.append("")
        lines.append("---")
        lines.append("## Questions below lecture videos (per lecture)")
        for path in lecture_files:
            raw = path.read_text(encoding="utf-8")
            head = raw.split("\n---\n", 1)
            head_text = head[0].lstrip("# ").split("\n")[0]
            content = head[1] if len(head) == 2 else raw
            if "(no questions below this lecture" in content and (
                    "Q1." not in content
                    and "QUESTION 1" not in content
                    and "Classroom Quiz" not in content):
                continue
            with_questions += 1
            lines.append("")
            lines.append("### " + head_text.strip())
            lines.append(content.strip())

    not_fetched = []
    lec_texts = []
    for sid in matched_sids:
        for path in LECTQ_DIR.glob(sid + "_*.md"):
            lec_texts.append(path.read_text(encoding="utf-8"))
    for quiz in quizzes:
        frag = str(quiz.get("title") or "").split(" - ")[0][:45].lower()
        if frag and not any(frag in text.lower() and "QUESTION 1/" in text
                            for text in lec_texts):
            not_fetched.append(str(quiz.get("title")))

    if not_fetched or matched_sids:
        lines.append("")
        lines.append("---")
        lines.append("## NOT FETCHED — open these yourself")
        lines.append("(These sit behind `Attempt Now` / `Start Test` "
                     "buttons. I never click those — they consume quiz "
                     "attempts. Everything else above is complete.)")
        if not_fetched:
            lines.append("")
            lines.append("### Revision quizzes whose questions never "
                         "became visible (" + str(len(not_fetched))
                         + ")")
            lines.append("(quiz window closed while unattempted — try "
                         "`Attempt Now` on that lecture's Assignments tab "
                         "yourself, or check My Assessments)")
            for title in not_fetched:
                lines.append("- " + title)
        lines.append("")
        lines.append("### Quiz Contests tab (separate MCQ tests)")
        lines.append("- Quiz contest questions only appear after "
                     "`Start Test` (graded, consumes an attempt): "
                     "open the Quiz Contests tab manually if you want "
                     "these: PSP Contest 1, Wifi Demo, Demo_Contest, "
                     "Mock Test")
        lines.append("- What IS captured: all assignment questions "
                     "(100), all in-class quiz questions shown above, "
                     "all contest ASSIGNMENT texts (PSP Contest 2)")

    lines.append("")
    lines.append("---")
    lines.append("TOTALS: " + str(total_q) + " assignment questions ("
                 + str(solved_q) + " solved), " + str(len(quizzes))
                 + " quizzes, " + str(len(no_text))
                 + " questions without captured text, "
                 + str(with_questions) + " lecture windows with content.")
    if no_text:
        lines.append("Missing text: " + "; ".join(sorted(set(no_text))))

    export_dir = BASE / "export"
    export_dir.mkdir(exist_ok=True)
    out_path = export_dir / (re.sub(r"[^A-Za-z0-9]+", "-", label).strip("-")
                             + "-questions.md")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("EXPORTED " + str(out_path))
    print("  assignments: " + str(len(assignments)) + " | questions: "
          + str(total_q) + " (" + str(solved_q) + " solved) | quizzes: "
          + str(len(quizzes)) + " | texts included: "
          + str(total_q - len(no_text)) + " | lecture windows: "
          + str(with_questions))
    return 0


# ---------- targets / subjects / discovery ----------

def read_lines(path):
    if not path.exists():
        return []
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")]


def subject_ids():
    ids = []
    for line in read_lines(SUBJECTS_FILE):
        ids.append(line.split("|")[0].strip())
    return ids


def subject_matrix():
    # The portal accepts &subject=<course-id> on the hub tabs: each URL then
    # renders THAT subject's own Overview/Lectures/Assignments/Quiz/Contest
    # (verified: own attendance, own questions, own quizzes).
    pages = []
    for sid in subject_ids():
        for sub in SUBTABS:
            pages.append("https://my.newtonschool.co/course/" + HUB
                         + "/details?tab=course&view-type=Weekly&subTab=" + sub
                         + "&subject=" + sid)
    for tab in ("student-calendar", "my-timeline", "mentor-help",
                "my-requests", "leaderboard"):
        pages.append("https://my.newtonschool.co/course/" + HUB
                     + "/details?tab=" + tab + "&view-type=Weekly")
    pages.append("https://my.newtonschool.co/course/" + HUB
                 + "/details?tab=course&view-type=Weekly")
    return pages


def link_ok(url):
    low = url.lower()
    if any(bad in low for bad in FORBIDDEN):
        return False
    if not any(host in low for host in ALLOWED_HOSTS):
        return False
    # only follow /course/ links for the hub or our own enrolled subjects
    match = re.search(r"/course/([a-z0-9]{8,})/", low)
    if match and match.group(1) != HUB and match.group(1) not in subject_ids():
        return False
    return True


def discover(links):
    known = set(read_lines(HOT_TARGETS)) | set(read_lines(COOL_TARGETS))
    if len(known) > 150:
        return []
    new = []
    for raw in links:
        url = raw.split(" :: ", 1)[-1].strip()
        base = url.split("#", 1)[0]
        if base not in known and link_ok(base):
            new.append(base)
    if new:
        with COOL_TARGETS.open("a", encoding="utf-8") as handle:
            for url in dict.fromkeys(new):
                handle.write(url + "\n")
                log("DISCOVERED new portal link -> " + url)
    return new


# ---------- cycles ----------

def run_cycle(deep=True, profile=PROFILE, hot_only=False):
    MATERIALS.mkdir(exist_ok=True)
    QUESTIONS.mkdir(exist_ok=True)
    hot = read_lines(HOT_TARGETS)
    if not hot:
        log("ERROR: no hot targets in " + str(HOT_TARGETS))
        return 1
    urls = list(hot)
    if deep and not hot_only:
        urls += subject_matrix()
        urls += read_lines(COOL_TARGETS)
    seen = set()
    urls = [u for u in urls if not (u in seen or seen.add(u))]

    problems = 0
    with sync_playwright() as pw:
        context = pw.chromium.launch_persistent_context(
            str(profile), channel="chrome", headless=True,
            viewport={"width": 1400, "height": 900}, args=STEALTH_ARGS,
        )
        context.add_init_script(STEALTH_JS)
        api_data, api_listener = make_api_collector()
        context.on("response", api_listener)
        page = (list(context.pages) or [context.new_page()])[0]
        state = load_qstate()
        budget = MAX_OPENS_PER_CYCLE if deep and not hot_only else 0
        spent = 0
        for url in urls:
            links = capture_target(page, url)
            discover(links)
            if budget and spent < budget and any(
                    marker in url for marker in OPENABLE):
                spent += open_questions(page, url, state, budget - spent)
        if state:
            save_qstate(state)
        if deep and not hot_only:
            lec_state = _load_json(LECTQ_STATE)
            lec_budget = 18
            for sid in subject_ids():
                if lec_budget <= 0:
                    break
                lec_budget -= harvest_lectures(page, sid, lec_state,
                                               lec_budget)
            if lec_state:
                LECTQ_DIR.mkdir(exist_ok=True)
                LECTQ_STATE.write_text(json.dumps(lec_state, indent=1),
                                       encoding="utf-8")
            log("Lecture harvest this cycle: " + str(18 - max(lec_budget, 0))
                + " lecture(s) checked")
        write_digest(api_data)
        try:
            context.close()
        except Exception:
            pass
    log("Cycle " + ("DEEP" if deep and not hot_only else "HOT")
        + " finished (" + str(len(urls)) + " pages, "
        + str(spent if deep and not hot_only else 0) + " opened).")
    return problems


def run_watch(interval, deep_every, profile=PROFILE):
    log("Watch daemon: hot every " + str(interval) + "s, deep every "
        + str(deep_every) + " cycles. Read-only.")
    cycle_no = 0
    while True:
        cycle_no += 1
        deep = (cycle_no % deep_every == 0)
        try:
            run_cycle(deep=deep or cycle_no == 1, profile=profile)
        except Exception as error:
            log("ERROR in cycle: " + str(error))
        time.sleep(interval)


def run_login_window(urls, profile):
    with sync_playwright() as pw:
        context = pw.chromium.launch_persistent_context(
            str(profile), channel="chrome", headless=False, no_viewport=True,
            args=STEALTH_ARGS + ["--window-size=1400,900"],
        )
        context.add_init_script(STEALTH_JS)
        pages = list(context.pages) or [context.new_page()]
        try:
            pages[0].goto(urls[0], wait_until="domcontentloaded", timeout=45000)
            for url in urls[1:]:
                pg = context.new_page()
                try:
                    pg.goto(url, wait_until="domcontentloaded", timeout=45000)
                except Exception:
                    pass
        except Exception:
            pass
        log("Login window open — sign in yourself (your eyes only). "
            "Sessions persist after you close it.")
        try:
            while context.pages:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        try:
            context.close()
        except Exception:
            pass
        log("Login window closed. Sessions saved.")


def selftest():
    MATERIALS.mkdir(exist_ok=True)
    data_url = ("data:text/html,<title>mentor-selftest</title>"
                "<p>capture selftest content - the background tracker reads "
                "page text and stores it for the studying AI. This sentence "
                "pads the body so the non-empty check passes.</p>")
    before = set(MATERIALS.glob("live_*.md"))
    hot_path = HOT_TARGETS
    old_hot = hot_path.read_text(encoding="utf-8") if hot_path.exists() else None
    hot_path.write_text(data_url + "\n", encoding="utf-8")
    cool_old = COOL_TARGETS.read_text(encoding="utf-8") if COOL_TARGETS.exists() else None
    COOL_TARGETS.write_text("# selftest\n", encoding="utf-8")
    subj_old = SUBJECTS_FILE.read_text(encoding="utf-8") if SUBJECTS_FILE.exists() else None
    SUBJECTS_FILE.write_text("# selftest\n", encoding="utf-8")
    try:
        run_cycle(deep=False, profile=TEST_PROFILE, hot_only=True)
    finally:
        if old_hot is None:
            hot_path.unlink(missing_ok=True)
        else:
            hot_path.write_text(old_hot, encoding="utf-8")
        if cool_old is None:
            COOL_TARGETS.unlink(missing_ok=True)
        else:
            COOL_TARGETS.write_text(cool_old, encoding="utf-8")
        if subj_old is None:
            SUBJECTS_FILE.unlink(missing_ok=True)
        else:
            SUBJECTS_FILE.write_text(subj_old, encoding="utf-8")

    fresh = set(MATERIALS.glob("live_*.md")) - before
    ok_text = any("capture selftest content" in p.read_text(encoding="utf-8")
                  for p in fresh)
    print(("PASS" if ok_text else "FAIL") + ": cycle writes live_ file with text")
    ok_png = any(p.with_suffix(".png").exists() for p in fresh)
    print(("PASS" if ok_png else "FAIL") + ": full-page screenshot saved")
    today = datetime.now().strftime("%Y%m%d")
    ok_archive = any("selftest" in p.name for p in
                     MATERIALS.glob("archive_" + today + "_*.md"))
    print(("PASS" if ok_archive else "FAIL") + ": daily archive written")
    ok_matrix = (len(subject_matrix()) ==
                 len(subject_ids()) * len(SUBTABS) + 6)
    print(("PASS" if ok_matrix else "FAIL") + ": subject matrix complete ("
          + str(len(subject_ids())) + " subjects x "
          + str(len(SUBTABS)) + " tabs + 6 hub pages)")

    for p in fresh:
        p.unlink(missing_ok=True)
        p.with_suffix(".png").unlink(missing_ok=True)
    for p in MATERIALS.glob("archive_" + today + "_*selftest*"):
        p.unlink(missing_ok=True)
        p.with_suffix(".png").unlink(missing_ok=True)
    return ok_text and ok_png and ok_archive and ok_matrix


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

    if flag("--export"):
        subject = value("--export", "")
        if not subject:
            print("Usage: scrape.py --export \"PSP B\"  (or a course id)")
            sys.exit(2)
        sys.exit(export_subject(subject))

    if flag("--lectures"):
        subject = value("--lectures", "")
        if not subject:
            print("Usage: scrape.py --lectures \"PSP B\"  (or 'psp' for"
                  " several at once)")
            sys.exit(2)
        sid = None
        matched = _matched_subjects(subject)
        if matched:
            sid = matched[0][0]
        if not sid and re.fullmatch(r"[a-z0-9]{8,}",
                                    subject.strip().lower()):
            sid = subject.strip().lower()
        if not sid:
            print("Unknown subject '" + subject + "'. Known:")
            for line in read_lines(SUBJECTS_FILE):
                print("  " + line)
            sys.exit(1)
        lec_state = _load_json(LECTQ_STATE)
        with sync_playwright() as pw:
            context = pw.chromium.launch_persistent_context(
                str(PROFILE), channel="chrome", headless=True,
                viewport={"width": 1400, "height": 900},
                args=STEALTH_ARGS)
            context.add_init_script(STEALTH_JS)
            page = (list(context.pages) or [context.new_page()])[0]
            visited = harvest_lectures(page, sid, lec_state, budget=99)
            try:
                context.close()
            except Exception:
                pass
        LECTQ_DIR.mkdir(exist_ok=True)
        LECTQ_STATE.write_text(json.dumps(lec_state, indent=1),
                               encoding="utf-8")
        files = list(LECTQ_DIR.glob(sid + "_*.md"))
        with_q = sum(1 for f in files
                     if "Q1." in f.read_text(encoding="utf-8")
                     or "QUESTION 1" in f.read_text(encoding="utf-8")
                     or "Classroom Quiz" in f.read_text(encoding="utf-8"))
        print("LECTURES checked: " + str(visited) + " | files: "
              + str(len(files)) + " | with questions: " + str(with_q))
        sys.exit(0)

    profile = Path(value("--profile", str(PROFILE)))

    if flag("--watch"):
        interval = int(value("--interval", "120"))
        deep_every = int(value("--deep-every", "10"))
        try:
            run_watch(interval, deep_every, profile)
        except KeyboardInterrupt:
            log("Watch daemon stopped.")
        sys.exit(0)

    if flag("--auto"):
        ok = run_cycle(deep=not flag("--hot"), profile=profile,
                       hot_only=flag("--hot"))
        sys.exit(0 if ok == 0 else 3)

    targets = [a for a in args if not a.startswith("--")]
    if not targets:
        print(__doc__)
        sys.exit(2)
    run_login_window(targets, profile)
