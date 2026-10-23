"""Harvest full message history of Slack channels (read-only) from the
scraper's logged-in session, using Slack's per-message data-item-id for
lossless merging across scroll windows.

Usage:
    .venv/bin/python slack_harvest.py                    # psp channels
    .venv/bin/python slack_harvest.py psp-b1 general-announcements-26
Output: materials/slack-questions/<channel>.md  (chronological messages)
Stop the launchd daemon first (profile lock): launchctl bootout
gui/$(id -u)/com.arush.mentor.watch
"""
import datetime
import json
import pathlib
import re
import sys

import scrape as S

OUT = pathlib.Path(__file__).parent / "materials" / "slack-questions"
DEFAULT_CHANNELS = ["psp-26", "psp-b1", "psp-b2"]
ITEM_JS = """() => {
  const out = {};
  const cards = Array.from(document.querySelectorAll('div.c-search_message'))
    .filter(c => !(c.parentElement
      && c.parentElement.closest('div.c-search_message')));
  const useCards = cards.length > 0;
  const src = useCards ? cards : Array.from(document.querySelectorAll('[data-ts]'));
  let i = 0;
  for (const el of src) {
    i++;
    let txt = (el.innerText || '').trim();
    if (!useCards) {
      let p = el.parentElement;
      for (let k = 0; k < 3 && p; k++) {
        const t = (p.innerText || '').trim();
        if (t.length > txt.length && t.length <= 3000) txt = t;
        p = p.parentElement;
      }
    }
    if (!txt) continue;
    const hrefs = Array.from(el.querySelectorAll('a[href]'))
      .map(a => a.getAttribute('href') || '')
      .filter(h => h && h.indexOf('slack-redir') === -1
        && h.indexOf('newtonschoolo-e998430.slack.com/archives') === -1);
    if (hrefs.length)
      txt += '\\nLINKS: ' + Array.from(new Set(hrefs)).join(' ');
    let tsEl = (el.matches && el.matches('[data-ts]')) ? el
      : el.querySelector('[data-ts]');
    const ts = tsEl ? (tsEl.getAttribute('data-ts') || '') : '';
    const id = /^\\d{10}/.test(ts) ? ts : ('fp:' + txt.slice(0, 120));
    if (!out[id] || txt.length > out[id].length)
      out[id] = {id, txt};
  }
  return Object.values(out);
}"""

SHOWMORE_JS = """() => {
  let n = 0;
  for (const b of document.querySelectorAll('button.c-search__expand')) {
    b.click(); n++;
  }
  for (const e of document.querySelectorAll('span,button,a,div')) {
    const t = (e.innerText || '').trim();
    if ((t === 'Show more' || t === 'Show more results')
        && e.children.length <= 3) { e.click(); n++; }
  }
  return n;
}"""

RESULTS_JS = """() => {
  const m = document.body.innerText.match(/(\\d[\\d,]*) results?/);
  return m ? parseInt(m[1].replace(/,/g, ''), 10) : null;
}"""


MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
     "Oct", "Nov", "Dec"], 1)}


def open_channel(page, channel, before=None):
    """Open Slack search with in:<channel> after:<start> and optional
    before:<date> window — server-side results give full messages
    (channel view lazy-loads only ~12). Search caps at 20 results per
    query, so callers re-query with narrower before: windows and merge.
    The default 'Last 7 days' filter is overridden by after:."""
    page.goto("https://app.slack.com/client/T0BNJRD9QT1/C0BS7CY7XV0",
              wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(9000)
    query = "in:" + channel + " after:2026-08-01"
    if before:
        query += " before:" + before
    # a search modal left open from a previous window blocks the
    # top-nav Search button — close it first
    dlg = page.locator(
        'div.ReactModalPortal [role="dialog"][aria-label="Search"]')
    for _ in range(3):
        try:
            if dlg.count() and dlg.first.is_visible():
                page.keyboard.press("Escape")
                page.wait_for_timeout(700)
            else:
                break
        except Exception:
            break
    try:
        page.locator('button[aria-label="Search"]').first.click(timeout=6000)
    except Exception:
        page.locator('button[aria-label="Search"]').first.click(
            timeout=6000, force=True)
    page.wait_for_timeout(1500)
    # make sure keystrokes land in the search input
    try:
        field = page.locator(
            'div.ReactModalPortal input, div.ReactModalPortal '
            '[contenteditable="true"]')
        if field.count() and field.first.is_visible():
            field.first.click(timeout=2000)
            page.wait_for_timeout(300)
    except Exception:
        pass
    page.keyboard.type(query, delay=45)
    page.wait_for_timeout(1200)
    page.keyboard.press("Enter")        # turns query into chips
    page.wait_for_timeout(800)
    page.keyboard.press("Enter")        # runs the search
    page.wait_for_timeout(8000)
    expand_snippets(page)
    return page.url


def oldest_date(items):
    """Bound for the next narrower before: query — the oldest card DATE
    LINE ('30 Sep at 3:53 PM'), never a date merely mentioned in a
    message body."""
    best = None
    pattern = re.compile(r"(\d{1,2}) (" + "|".join(MONTHS) + r") at ")
    for txt in items.values():
        m = pattern.search(txt[:400])
        if not m:
            continue
        key = (MONTHS[m.group(2)], int(m.group(1)))
        if best is None or key < best:
            best = key
    if not best:
        return None
    month, day = best
    nxt = datetime.date(2026, month, day) + datetime.timedelta(days=1)
    return nxt.isoformat()


def expand_snippets(page, cap=60):
    """Long messages truncate to '... Show more' in results — expand them
    (read-only) so statements are complete."""
    for _ in range(cap):
        if page.evaluate(SHOWMORE_JS) == 0:
            break
        page.wait_for_timeout(350)


FIND_SCROLLER_JS = """() => {
  let best = null;
  for (const e of document.querySelectorAll('div')) {
    if (e.closest('[class*="p-channel_sidebar"]')) continue;
    const s = getComputedStyle(e);
    if ((s.overflowY === 'auto' || s.overflowY === 'scroll')
        && e.scrollHeight > e.clientHeight + 100) {
      if (!best || e.scrollHeight > best.scrollHeight) best = e;
    }
  }
  if (!best) return false;
  best.setAttribute('data-harvest-scroller', '1');
  return true;
}"""

SCROLL_JS = """(step) => {
  const el = document.querySelector('[data-harvest-scroller="1"]');
  if (!el) return null;
  const max = Math.max(0, el.scrollHeight - el.clientHeight);
  const before = el.scrollTop;
  el.scrollTop = Math.min(max, Math.max(0, before + step));
  return {before, after: el.scrollTop, top: el.scrollTop === 0,
          bottom: el.scrollTop >= max - 2};
}"""


def collect(page, rounds=160):
    """Results sort newest-first (scroll DOWN loads older pages); channel
    view sorts newest-last (scroll UP loads older). Real wheel events are
    required — Slack's lazy loading ignores programmatic scrollTop.
    Every card seen along the way is merged by timestamp."""
    found = page.evaluate(FIND_SCROLLER_JS)
    if not found:
        print("  note: no scrollbar (few results) — capturing mounted "
              "cards only")
    box = page.evaluate("""() => {
      const el = document.querySelector('[data-harvest-scroller="1"]');
      if (!el) return null;
      const r = el.getBoundingClientRect();
      return {x: r.x + r.width / 2, y: r.y + r.height / 2}; }""")
    items = {}
    last_size = -1
    stable = 0

    def snap():
        for it in page.evaluate(ITEM_JS):
            if it["txt"] and (it["id"] not in items
                              or len(it["txt"]) > len(items[it["id"]])):
                items[it["id"]] = it["txt"]

    snap()
    if box:
        page.mouse.move(box["x"], box["y"])
    for direction in (1, -1):
        stable = 0
        for _ in range(rounds):
            if box:
                page.mouse.wheel(0, 800 * direction)
            page.wait_for_timeout(700)
            page.evaluate(SHOWMORE_JS)
            snap()
            grew = len(items) != last_size
            last_size = len(items)
            stable = 0 if grew else stable + 1
            state = page.evaluate(SCROLL_JS, 0)
            if not state:
                break
            reached = (state.get("bottom") if direction > 0
                       else state.get("top"))
            if reached and stable >= 10:
                break
            if stable >= 40:
                break
    snap()
    return items


def expand_threads(page, items, cap=40):
    """Click 'N replies' triggers (read-only) and merge thread messages."""
    opened = 0
    while opened < cap:
        triggers = page.get_by_text(re.compile(r"^\d+ repl(y|ies)$"))
        n = triggers.count()
        done_all = True
        for i in range(n):
            try:
                trig = triggers.nth(i)
                trig.scroll_into_view_if_needed(timeout=2000)
                trig.click(timeout=3000)
                page.wait_for_timeout(1800)
                before = len(items)
                for it in page.evaluate(ITEM_JS):
                    if it["id"] not in items and it["txt"]:
                        items[it["id"]] = it["txt"]
                opened += 1
                if len(items) > before:
                    done_all = False
                if opened >= cap:
                    break
            except Exception:
                continue
        if done_all or opened >= cap:
            break
        page.keyboard.press("Escape")
        page.wait_for_timeout(600)
    try:
        page.keyboard.press("Escape")
    except Exception:
        pass
    return items


def sort_key(item_id):
    first = re.match(r"(\d{10})", item_id)
    return (int(first.group(1)) if first else 0, item_id)


def harvest(channel, threads=False):
    """Query the channel, then keep re-querying with narrower before:
    windows (search returns max 20 per query) until every result Slack
    reports is collected."""
    all_items = {}
    expected = None
    used_before = set()
    no_growth_rounds = 0
    failures = 0
    url = ""
    for attempt in range(40):
        before = None if attempt == 0 else oldest_date(all_items)
        if before and before in used_before:
            # a single day filled the whole 20-result page — step past it
            steps = 0
            while before and before in used_before and steps < 90:
                before = (datetime.date.fromisoformat(before)
                          - datetime.timedelta(days=1)).isoformat()
                steps += 1
            if not before or before in used_before:
                break
        if before:
            used_before.add(before)
        with S.sync_playwright() as pw:
            ctx = pw.chromium.launch_persistent_context(
                str(S.PROFILE), channel="chrome", headless=True,
                viewport={"width": 1500, "height": 950},
                args=S.STEALTH_ARGS)
            ctx.add_init_script(S.STEALTH_JS)
            page = (list(ctx.pages) or [ctx.new_page()])[0]
            url = open_channel(page, channel, before=before)
            if S.looks_logged_out(page):
                print("ACTION NEEDED: Slack session expired — open a "
                      "login window (MENTOR.md §6)")
                try:
                    ctx.close()
                except Exception:
                    pass
                break
            items = collect(page)
            exp_this = page.evaluate(RESULTS_JS)
            try:
                ctx.close()
            except Exception:
                pass
        if exp_this is None and not items:
            failures += 1
            if before:
                used_before.discard(before)
            print("  window", attempt + 1, "failed to render — retrying ("
                  + str(failures) + ")")
            if failures >= 4:
                break
            continue
        failures = 0
        if expected is None:
            expected = exp_this
        before_count = len(all_items)
        for key, txt in items.items():
            if key not in all_items or len(txt) > len(all_items[key]):
                all_items[key] = txt
        grew = len(all_items) > before_count
        print("  window", attempt + 1,
              ("before " + before) if before else "(newest)",
              "->", len(items), "cards; total", len(all_items),
              "| this query reports:", exp_this,
              "" if grew else "[no growth]")
        if expected and len(all_items) >= expected:
            break
        if not grew and attempt >= 1:
            no_growth_rounds = no_growth_rounds + 1
            if no_growth_rounds >= 2:
                break
        else:
            no_growth_rounds = 0
    items = all_items
    OUT.mkdir(exist_ok=True)
    lines = ["# Slack #" + channel, "URL: " + url,
             "Captured: " + datetime.datetime.now().isoformat(
                 timespec="seconds"),
             "Messages: " + str(len(items)),
             "Results reported by Slack: " + str(expected), "---", ""]
    for item_id in sorted(items, key=sort_key):
        lines.append(items[item_id])
        lines.append("")
    (OUT / (channel + ".md")).write_text("\n".join(lines), encoding="utf-8")
    note = ""
    if isinstance(expected, int) and expected > len(items):
        note = "  ** PARTIAL: Slack reports " + str(expected) + " results **"
    print(channel, "->", len(items), "messages (Slack says", expected, ")",
          note)
    return len(items)


if __name__ == "__main__":
    chans = sys.argv[1:] or DEFAULT_CHANNELS
    want_threads = "--threads" in chans
    chans = [c for c in chans if c != "--threads"]
    total = 0
    for ch in chans:
        total += harvest(ch, threads=want_threads)
    print("TOTAL messages:", total)
