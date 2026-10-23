# Study material lives here (AI reads it all)

**Automatic, continuous** — the background daemon (`scrape.py --watch`)
writes:

- `live_<page>.md` + `.png` — current state of every portal/Slack page
  (hot pages every 2 min, every subject × every tab every ~20 min).
  Overwritten each cycle, so it is always "now".
- `archive_YYYYMMDD_<page>.md` — first capture of each day = history.
- `questions/live_<id>.md` — full text of assignment/quiz items (the
  tracker clicks the row, reads the opened tab, closes it).
- `api/digest.md` (+ `api/archive_*`) — per-subject assignments
  (in-class/post-class, solved status, deadlines), quiz schedules,
  attendance totals — from the portal's own responses.
- `captures.log` (in the repo root) — timeline + `ACTION NEEDED` alerts.

**Manual** — `./refresh.sh` runs one full sweep immediately.

The AI reads every `.md` (and `.png`) here directly from this Mac.
PDFs, your own screenshots, or plain-text notes dropped into files also
belong here.

NEVER put passwords, tokens, or login files in this folder.
