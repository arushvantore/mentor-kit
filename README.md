# Mentor Kit — your AI mentor with live portal + Slack awareness

> Hand this repo to ANY AI assistant (with file access on this Mac) and say:
> **"Read MENTOR.md, then teach me {subject} — exam on {date}."**
> It will know your assignments, quizzes, Slack announcements, your
> progress, your weak areas — and it will run the whole study loop.

**Creator:** arush ([@arushvantore](https://github.com/arushvantore))
**Repo:** this one (private — contains tooling, not your personal captures)
**Sister project:** `schedule_planner` (the daily-plan engine — separate)

**▶ The 60-second launch film** — schedule_planner, real terminal output,
real data (nothing staged). Click the preview to play **[launch.mp4](./launch.mp4)**:

[![schedule_planner launch film preview](./preview.gif)](./launch.mp4)

---

## How anyone can use this (the finished product)

This is the finished product. Anyone who wants to use it just:

1. Opens **Open WebUI**.
2. Goes to **http://localhost:3000**.
3. Picks a model.
4. Sends a message like:

**"Read MENTOR.md, then teach me DBMS — exam on {date}."**

The AI reads the mentor kit and teaches.

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

# 2. One full sweep now (all subjects + opens every assignment question)
./refresh.sh

# 3. Background daemon (installed via launchd — see below)
launchctl load ~/Library/LaunchAgents/com.arush.mentor.watch.plist
```

Then open a chat with any AI and paste one of the orders in
[`MENTOR.md`](MENTOR.md) §Order Examples.

---

## The commands

| Command | What it does | When |
|---|---|---|
| `.venv/bin/python scrape.py --watch` | Background daemon: **hot pages every 2 min** (dashboard, all assignments, all quizzes, question of the day, Slack) + **deep sweep every ~20 min** (every subject × every tab + opens new assignment/quiz rows to read them) | Always (launchd) |
| `./refresh.sh` | One manual full sweep → `materials/live_*.md` | On demand |
| `.venv/bin/python scrape.py --auto --hot` | One hot-only sweep | On demand |
| `.venv/bin/python scrape.py --export "PSP B"` | One file with **every question of one subject** (in-class, post-class, contests, solved, due — full texts) → `export/<subject>-questions.md` | On demand (hand it to a teaching AI) |
| `.venv/bin/python export_html_pdf.py export/PSP-questions.md` | Render that file to **HTML + PDF** for sharing; public copy lives at https://arushvantore.github.io/psp-questions/ (push 3 files to repo `psp-questions`) | After an export changes |
| `.venv/bin/python scrape.py --lectures "PSP"` | Harvest **everything under each lecture video** (in-class quiz questions via read-only views, post-class texts, `Read More` expanded) → `materials/lecture-questions/` (picked up by `--export`) | On demand; deep cycles repeat it (24 h per lecture) |
| `.venv/bin/python slack_harvest.py [channel …]` | Full text of every message in #psp-26/#psp-b1/#psp-b2 via read-only Slack search (snippets expanded, counts must match Slack's) → `materials/slack-questions/` (picked up by `--export`) | On demand; after the teacher posts new questions/links |
| `.venv/bin/python scrape.py <url> ...` | Login window (visible Chrome, **no button**) — sign in yourself, close when done | Only if a session expires |
| `.venv/bin/python scrape.py --selftest` | Offline end-to-end check (4 PASS expected) | After setup or changes |

## What the AI can see (`materials/`)

- `live_<page>.md/.png` — **current** state of every portal page:
  every subject's Overview/Lectures/Assignments/Quiz/Contest (URL carries
  `&subject=<id>`), attendance ("10/12 Attended" + per-lecture column),
  global all-assignables, Calendar, Timeline, Slack, dashboard.
- `archive_YYYYMMDD_<page>.md` — daily history (**past** activity).
- `questions/live_<id>.md` — full text of assignment questions, opened
  automatically by clicking the row in a new tab, read, then closed.
- `api/digest.md` — per-subject assignments/quizzes with in-class/post-class
  tags, solved status, deadlines (from the portal's own API responses).
- `captures.log` — timeline + `ACTION NEEDED` alerts.

## Background automation (installed & running)

`launchd/com.arush.mentor.watch.plist` keeps `scrape.py --watch` alive
(hot every 120 s, deep every 10th cycle). Reboots: `RunAtLoad` restarts it.

**Honest caveat:** if a site logs you out, cycles write
`ACTION NEEDED: ...` into `captures.log` instead of saving a login page.
Fix takes one minute: run the login-window command, sign in, close.

---

## Safety rules (baked into the design)

1. **Read-only** — the capturer never types, never submits, never starts a
   test, never uploads. It clicks only to *open and read* pages/rows
   (question text), then closes what it opened.
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
mentor-kit/  (~/exam-prep, Desktop link: ~/Desktop/exam-prep)
├── README.md        ← you are here (system overview + commands)
├── MENTOR.md        ← THE playbook any AI reads first (order examples,
│                       daily loop, teaching method, hard rules)
├── PLAN.md          ← day-by-day study plan (AI maintains)
├── STATUS.md        ← honest progress tracker (AI maintains every session)
├── scrape.py        ← the read-only tracker (watch/auto/login/selftest)
├── subjects.txt     ← all enrolled course ids (per-subject windows)
├── targets-hot.txt  ← pages refreshed every 2 min
├── targets.txt      ← cool pages + auto-discovered portal links
├── watch.sh         ← daemon entry point
├── refresh.sh       ← one manual full sweep
├── launchd/         ← com.arush.mentor.watch.plist (installed)
├── btech-sem1/      ← B.Tech Sem 1 Master Knowledge System (study material + syllabus)
├── materials/       ← captures + questions/ + api/ (AI reads; gitignored)
├── NOTES/           ← AI-written revision notes per topic (gitignored)
├── captures.log     ← tracker log incl. ACTION NEEDED alerts (gitignored)
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
