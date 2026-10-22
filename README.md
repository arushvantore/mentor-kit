# Mentor Kit — your AI mentor with live portal + Slack awareness

> Hand this repo to ANY AI assistant (with file access on this Mac) and say:
> **"Read MENTOR.md, then teach me {subject} — exam on {date}."**
> It will know your assignments, quizzes, Slack announcements, your
> progress, your weak areas — and it will run the whole study loop.

**Creator:** arush ([@arushvantore](https://github.com/arushvantore))
**Repo:** this one (private — contains tooling, not your personal captures)
**Sister project:** `schedule_planner` (the daily-plan engine — separate)

---

## How it works (the whole idea)

```
┌─ YOUR WORLD (your logins only) ──────────────────────────────┐
│  College portal: assignments, quizzes, weekly course content │
│  Slack: class channel announcements, quizzes, deadlines      │
└───────────────┬──────────────────────────────────────────────┘
                │  read-only capturer (scrape.py)
                │  YOU log in; script only reads; nothing uploads
                ▼
   exam-prep/materials/  ── local .md + .png snapshots
                │  any AI reads these files directly
                ▼
   THE MENTOR (any AI, following MENTOR.md)
     · knows what's new (assignments/quizzes/announcements)
     · makes PLAN.md (exam − 5 buffer, weak topics first)
     · teaches topic-by-topic, doubts welcome
     · writes revision notes into NOTES/
     · quizzes recall-first, honest readiness
     · updates STATUS.md every session
                │
                ▼
   YOU: "teach me DBMS" → real teaching against YOUR real syllabus
```

**The AI never sees your passwords.** Logins live in `.browser-profile/`
on this Mac only (gitignored, never pushed, never read by the AI).

---

## Quick start (fresh machine / new AI)

```sh
# 1. Setup (once)
python3 -m venv .venv
.venv/bin/pip install playwright
.venv/bin/playwright install chromium
.venv/bin/python scrape.py --selftest     # expect: 4 × PASS

# 2. Interactive capture (deep browsing, old quizzes, long threads)
.venv/bin/python scrape.py "https://your-portal-url" "https://app.slack.com/..."

# 3. Daily auto refresh (newest content from targets.txt, headless)
./refresh.sh
```

Then open a chat with any AI and paste one of the orders in
[`MENTOR.md`](MENTOR.md) §Order Examples.

---

## The three commands

| Command | What it does | When |
|---|---|---|
| `./refresh.sh` | Headless capture of every URL in `targets.txt` → `materials/auto_*.md` | Daily (auto via launchd — see below) |
| `.venv/bin/python scrape.py <url> ...` | Opens a window; **you** browse & click the blue CAPTURE button per page | When you want deep/old content or a session expired |
| `.venv/bin/python scrape.py --selftest` | Offline end-to-end check (4 PASS expected) | After setup or changes |

## Daily automation (every new day, no disturbance)

`launchd/com.arush.mentor.refresh.plist` runs `refresh.sh` every day at
**7:10 AM** — new portal data, new Slack messages, saved while you sleep.

**Not installed on purpose.** To turn it on (one time, by hand):

```sh
# edit the two REPLACE_WITH_REPO_PATH lines inside the plist first
cp launchd/com.arush.mentor.refresh.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.arush.mentor.refresh.plist
```

**Honest caveat:** if a site logs you out, that day's run writes
`ACTION NEEDED: ...` into `captures.log` instead of saving a login page.
Fix takes one minute: run the interactive command, log in, close.

---

## Safety rules (baked into the design)

1. **Read-only** — the capturer never types, never clicks site buttons,
   never submits, never uploads. It only reads what you're viewing.
2. **Credentials stay local** — `.browser-profile/` (gitignored). The AI
   does not read it. Nobody should ever ask you for a password here.
3. **This repo is PRIVATE** — it holds tooling + progress files.
   Personal captures in `materials/` are gitignored (local only) as an
   extra layer; they stay available to any AI working on this Mac.
4. **No fake precision** — the mentor reports "behind/on pace" honestly,
   never invented percentages or false greens.
5. **Ask before installs** — any new package needs your yes first.

---

## Folder map

```
mentor-kit/  (exam-prep on your Desktop)
├── README.md        ← you are here (system overview + commands)
├── MENTOR.md        ← THE playbook any AI reads first (order examples,
│                       daily loop, teaching method, hard rules)
├── PLAN.md          ← day-by-day study plan (AI maintains)
├── STATUS.md        ← honest progress tracker (AI maintains every session)
├── scrape.py        ← the read-only capturer (interactive + --auto + selftest)
├── targets.txt      ← URLs the daily refresh captures
├── refresh.sh       ← daily auto-capture entry point
├── launchd/         ← 7:10 AM daily-refresh template (not installed)
├── materials/       ← capture snapshots + your own drops (AI reads; gitignored)
├── NOTES/           ← AI-written revision notes per topic (gitignored)
├── captures.log     ← capturer log incl. ACTION NEEDED alerts (gitignored)
├── .venv/           ← private python env (gitignored)
└── .browser-profile/ ← YOUR sessions live here (gitignored, never read)
```

---

## For an AI picking this up cold

1. Read [`MENTOR.md`](MENTOR.md) fully — it defines your job.
2. Read `STATUS.md` + `PLAN.md` — where the student is.
3. `ls -t materials/*.md` — read the newest 3–5 for what's fresh.
4. If subject/exam date unknown → ask ONE question, then start.
5. Run the loop in MENTOR.md §Daily Loop. Update `STATUS.md` before
   ending any session. Never leave the tracker stale.
