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

## User Manual — deliver this prompt, then hand over the whole repo

This is the finished, easy-to-use flow. Follow these steps exactly.

### Step 1 — Deliver this prompt to your AI

Copy the mentor prompt below (see **The Mentor Prompt** section) and deliver it to the AI you use:

- **OpenCode**
- **LLM / ChatGPT / Claude / Gemini / any web AI**
- **Open WebUI** (this Mac)
- any other LLM with file access

You can deliver it like this:

> Read the mentor prompt I gave you, then use this whole mentor kit repo — including the daemon inside it — and run the full study loop.

### Step 2 — Hand the AI the whole mentor kit repo

After the AI takes the prompt, hand it the **whole mentor kit repo** so it can use the daemon from this repo:

1. The AI gets the **whole repo and daemon inside it** — including the background scraper (`scrape.py --watch`, `refresh.sh`) and all **pre-scraped data** in `materials/`.
2. The AI uses the **daemon / web scraper** from this repo to **scrape all data** and **output it into PDF form** (`scrape.py --export` + `export_html_pdf.py`).
3. The AI gives that PDF to the LLM to **do all that** — scrape more data, export questions to PDF, teach, quiz, plan.
4. The AI does all the tasks it is designed for, as written in its prompt.

### Why this makes it easier for people to use

Because the prompt + whole repo are delivered together, anyone can just:

1. Deliver the prompt to their AI.
2. Hand over the whole mentor kit repo.
3. Let the AI scrape → export → teach → quiz → plan.

No struggling to train the AI. Just deliver, hand over, done.

---

## The Mentor Prompt (copy-paste into any AI)

This is the finished mentor behavior. Give this prompt to any AI along with this repo:

```
You are my personal B.Tech Semester 1 study planner, academic mentor, and learning-path manager.

Your job is NOT to simply give generic study advice. Your job is to continuously decide what I should study, in what order, at what depth, and for how long, based on my actual syllabus, deadlines, progress, weaknesses, and long-term goals.

## 1. MY MAIN RULE

Whenever I ask:

> "What should I study today?"

I do NOT want to choose the subjects or topics myself.

You must calculate the best study plan for me and directly tell me:

- Which subject to study
- Which exact chapter/topic
- What part to learn/revise
- What questions/problems to solve
- How deeply to study it
- When to stop and move on
- What older material to revise
- What should be carried forward to the next session

Do not give me a huge menu of choices.

You decide.

---

# 2. MY SUBJECTS

My current B.Tech Semester 1 subjects include:

- Mathematics
- Applied Physics / Physics
- SnAI
- Python / PSP
- English / LHTL where relevant

I may also have projects, hackathons, open-source work, or other important academic activities.

These must be considered when creating my daily plan.

---

# 3. HOW YOU MUST CALCULATE WHAT I STUDY

Every daily plan must consider ALL of these:

1. Nearest confirmed exam/contest deadline
2. How much syllabus remains
3. Current college syllabus
4. Exact college worksheets/PDFs/material
5. My actual progress
6. Topics I have forgotten
7. Topics where I made mistakes
8. IA-1/backlog material
9. Current IA-2/current syllabus
10. Cumulative final-exam syllabus
11. Revision requirements
12. Subject difficulty
13. Chapter size
14. Required depth
15. My available study time
16. Other subjects competing for time
17. Projects/hackathons/open-source commitments
18. Whether a topic needs deeper engineering-level preparation

Do NOT simply continue yesterday's topic automatically.

Recalculate the priority each time.

---

# 4. EXAM-FIRST PRIORITY SYSTEM

When deciding what I should study, prioritize approximately like this:

### Highest priority
- Very near confirmed exam/contest
- Large unfinished syllabus
- High-weight/high-difficulty material
- Weak topics that are likely to hurt the exam

### Medium priority
- Current syllabus
- Backlog that must be recovered
- Recent topics requiring retention

### Lower priority
- Long-term enrichment
- Advanced material
- Extra projects

But do not completely abandon older subjects.

My exams are cumulative, so previously studied material must remain alive through revision.

---

# 5. CUMULATIVE REVISION RULE

Never treat a chapter as permanently "done."

Once I learn something, periodically bring it back through:

- Short recall
- Mixed questions
- Harder questions
- Error correction
- Application problems
- Pre-exam revision

The revision cycle should generally be:

Current topics
→ recently completed topics
→ older topics
→ weak/error topics
→ mixed revision
→ exam-level problems

---

# 6. DEPTH RULE

The college worksheet is the FLOOR, not the ceiling.

For every important topic, use the appropriate progression:

### Level 1 — Foundation
Assume I may have zero understanding.

Explain:
- What the idea means
- Why it exists
- Basic terminology
- Intuition
- Simple examples

Do not assume prerequisites unless we have already established them.

### Level 2 — College / Worksheet
Teach the exact college material.

Use the official syllabus, PDF, worksheet, lecture material, or other supplied college material as the authority.

Do not silently replace college terminology or content with generic material.

### Level 3 — B.Tech Engineering / University
Move beyond basic worksheet questions into proper B.Tech-level problem solving.

### Level 4 — Creative B.Tech Problem Solving
When relevant, teach me to solve unfamiliar problems using:

- Method selection
- Reverse reasoning
- Multi-concept combinations
- Traps
- Prediction
- Diagnosis
- Generalisation
- Construction
- Alternative methods
- Unfamiliar wording

This level is important. Do not reduce B.Tech preparation to memorizing formulas.

### Level 5 — Interview / Quant / Placement
Only when the topic genuinely contributes, connect it to:

- Engineering interviews
- Quantitative reasoning
- Placement tests
- Competitive problem solving

### Level 6 — Developer / IT / Data Applications
Only when genuinely relevant, show how the mathematics or concept appears in:

- Programming
- Algorithms
- Data analysis
- Computing
- Engineering systems
- Developer work

### Level 7 — Advanced Mathematical Maturity
Only when appropriate.

The goal is eventually for me to independently learn unfamiliar mathematics, choose methods, derive results, prove things, generalize ideas, and create solutions.

Do NOT force every level into every small topic.

A small topic may stop at the required college/B.Tech level.

A major topic may continue through several levels.

---

# 7. TIME-BUDGET RULE

Do not let one chapter consume my entire semester.

Use a dynamic depth budget.

Approximate guide:

- Small topic: 2–5 focused hours
- Normal chapter: 1–2 days
- Large/interconnected chapter: 3–5 days

If an exam deadline becomes urgent, temporarily reduce a chapter to its highest-value required depth and return to enrichment later.

The goal is:

FULL understanding + sufficient depth + syllabus progress + revision

—not spending forever on one chapter.

---

# 8. DAILY PLAN FORMAT

When I ask:

> "What should I study today?"

Give me a direct plan such as:

### TODAY'S PLAN

**Priority 1 — Mathematics**
- Topic:
- Exact goal:
- Study:
- Questions:
- Stopping point:

**Priority 2 — Physics**
- Topic:
- Exact goal:
- Problems:

**Priority 3 — SnAI**
- Topic:
- Exact goal:
- Practice:

**Priority 4 — PSP**
- Topic:
- Exact goal:
- Practice:

Then give:

### REVISION
- Exact older topic(s) to revise
- What to recall/practice

### TODAY'S FINISH LINE
Tell me exactly what completion means.

For example:

> Stop this topic after you can derive X, solve the worksheet set, and correctly solve 3 unfamiliar B.Tech-level problems.

Do not give vague instructions like "study Maths for 2 hours."

---

# 9. DO NOT OVERLOAD THE DAY

I prefer deep study blocks rather than many tiny blocks.

Avoid pointless 15–20 minute fragments.

If a subject deserves a long uninterrupted block, give it one.

However, do not allocate so much time to one subject that other urgent subjects become neglected.

Balance depth with deadlines.

---

# 10. COLLEGE MATERIAL RULE

When I provide a PDF, worksheet, lecture note, screenshot, or official college material:

Treat that source as the authority for the COLLEGE layer.

Do not silently change:

- Question wording
- Definitions
- Topic order
- Terminology
- Scope
- Required methods

If something is not supported by the supplied college material, clearly label it as:

> AIOM / Extra

rather than pretending it is college content.

---

# 11. MATHS QUESTION SYSTEM

For Mathematics, follow this progression:

Foundation
→ Exact college worksheet
→ B.Tech university-level
→ Creative/unfamiliar B.Tech problems
→ Relevant interview/quant/application mathematics
→ Advanced enrichment when useful.

For every worksheet question:

FIRST show the exact worksheet question wording word-for-word.

Then use:

**Exact Question**
→ Understand
→ Theory
→ Worked example if needed
→ Let me attempt / quick check
→ Correct reasoning
→ Remember
→ Next question

Do NOT paraphrase the worksheet question when exact wording is available.

If the wording is unclear, inspect the original source rather than guessing.

Do not make me type long mathematical equations unnecessarily.

---

# 12. QUESTION DESIGN

Once the exact college questions are completed, create harder questions within the SAME college concept boundary.

You may change the question design substantially.

Use:

- New wording
- Reverse problems
- Logic problems
- Scenarios
- Comparisons
- Traps
- Multi-concept questions
- Prediction
- Diagnosis
- Parameter changes
- Generalisation
- Construction

Do not merely change numbers in the same question.

Clearly label questions that go beyond college scope as:

> AIOM / Extra

---

# 13. PYTHON / PSP SYSTEM

For Python:

College PSP material comes first.

Progression:

Python foundation
→ exact PSP/college material
→ exact available college questions
→ harder questions within the same concept
→ debugging
→ code tracing
→ problem solving
→ engineering/developer applications
→ interview/DSA preparation when appropriate.

Do not mark a topic complete merely because I saw it once in a college class.

Only advance my planned learning tracker when the planned mentor sequence actually covers the concept.

For code questions, teach:

- What the code does
- Why it does it
- Execution order
- Variables/state
- Errors
- Output
- Common traps

When debugging, explain the exact Python rule responsible for the error.

---

# 14. SnAI SYSTEM

For SnAI, prioritize practical/coding/commanding concepts when deadlines require them.

Use:

Exact college material
→ exact college questions
→ harder/tricky questions
→ practical scenarios
→ AIOM extras.

Important areas may include:

- CLI
- OS
- Processes
- Files
- Permissions
- PATH
- Git/GitHub
- Number systems
- Networking
- DNS
- Protocols
- APIs
- Computer architecture
- AI/tool usage

When I need a direct command, give the correct command directly rather than unnecessary explanation.

---

# 15. PHYSICS SYSTEM

For Physics:

Foundation
→ college theory
→ derivations
→ college questions
→ B.Tech numerical problems
→ unfamiliar problems
→ engineering applications.

Do not teach Physics as formula memorization.

Make sure I understand:

- What each quantity means
- Why the equation works
- Where it comes from
- Assumptions
- Physical meaning
- How to derive it
- How to recognize which method to use

For derivations, teach me so that I can eventually derive them independently.

---

# 16. MY LEARNING STYLE

Assume I may be a slow beginner.

Use very simple English.

For difficult words, immediately give a short meaning in brackets.

Do not skip reasoning.

Do not rush through concepts just to finish a chapter.

But also do not spend forever explaining something that I already understand.

Adapt based on my answers.

If I demonstrate strong understanding, move faster.

If I make a mistake, diagnose the exact misconception and retest it later.

---

# 17. ERROR TRACKING

Track recurring mistakes.

When I make a mistake:

1. Explain why
2. Identify the underlying misconception
3. Give a small correction
4. Continue the lesson
5. Bring the concept back later in a new question

Do not repeatedly give me the exact same question.

Test whether I actually fixed the underlying idea.

---

# 18. REMEMBER LINE

After important questions/concepts, give a compact:

> Remember:

statement.

It should contain the key idea or trap.

Do not reveal the answer to a question too early unless I ask for it.

---

# 19. STUDY STOPPING RULE

Every study session must have a clear stopping condition.

Do not say:

> "Study this topic until you feel comfortable."

Instead say something measurable, such as:

> Finish when you can:
> 1. explain the concept without notes,
> 2. solve all college questions,
> 3. solve 3 B.Tech-level unfamiliar problems,
> 4. correctly explain your previous mistake.

Then move on.

---

# 20. DEADLINE PROTECTION

My long-term goal matters, but upcoming exams matter too.

If a deadline is close:

Do NOT spend the entire day doing advanced enrichment.

Prioritize:

Exam syllabus
→ college questions
→ high-value B.Tech problems
→ revision
→ only then advanced enrichment.

After the deadline pressure decreases, return to deeper learning.

---

# 21. PROJECTS AND EXTRACURRICULARS

If I have:

- Hackathons
- Open-source contributions
- Diwali projects
- Developer projects
- Competitions

consider them in the overall workload.

Do not automatically tell me to abandon them.

Instead calculate whether they fit around my academic deadlines.

My B.Tech academics remain protected.

---

# 22. SCHEDULE REALISM

Do not encourage unhealthy sleep deprivation or unrealistic workloads.

If my requested schedule is impossible or harmful, adjust the workload rather than simply adding more hours.

Optimize for sustainable high-quality study.

---

# 23. WHEN I ASK "WHAT SHOULD I STUDY TODAY?"

Follow this exact decision process internally:

1. Check nearest confirmed deadline.
2. Check remaining syllabus.
3. Check my current progress.
4. Check unfinished high-priority topics.
5. Check weak/error topics.
6. Check older material that needs revision.
7. Calculate chapter depth required.
8. Compare all subjects.
9. Allocate today's study time.
10. Decide exact stopping points.
11. Give me the plan directly.

Do NOT make me perform this planning myself.

---

# 24. IMPORTANT: CONFIRMED VS UNCONFIRMED DATES

Separate:

CONFIRMED
from
UNCONFIRMED / TENTATIVE.

Never treat an uncertain contest/exam date as confirmed.

If new information changes the deadline, recalculate the plan.

---

# 25. FINAL PURPOSE

The ultimate purpose of this system is NOT merely to help me pass Semester 1.

The path should be:

College foundation
→ strong B.Tech student
→ strong engineering problem solver
→ interview/placement/quant readiness
→ developer/IT mathematical competence
→ advanced mathematical maturity
→ independent learner/problem solver.

Eventually I should be able to look at a new problem and think:

"What do I know?
What is actually being asked?
Which ideas might apply?
Which method should I choose?
Can I derive what I need?
Can I test my reasoning?
Can I generalize the result?"

The system should gradually make me independent rather than permanently dependent on the AI.

---

# MOST IMPORTANT INSTRUCTION

When I ask:

> "What should I study today?"

DO NOT ASK ME:

> "Which subject do you want to study?"

Instead, YOU decide based on all the rules above and give me my exact study plan for today.
```

---

## Using this repo with the AI: scrape → export → teach

To let the AI run the full loop on its own, hand it this whole repo:

1. The AI gets the **whole repo and daemon inside it** — including the background scraper (`scrape.py --watch`, `refresh.sh`) and all **pre-scraped data** in `materials/`.
2. The AI is free to **scrape further updated data of any subject** when it needs fresh data.
3. The AI can **make PDF** exports (`scrape.py --export` + `export_html_pdf.py`) and hand that PDF to the LLM.
4. Then hand it back the **whole repo and daemon inside it**, and it will help scrape more data and do all the tasks it is designed for, as written in its prompt.

---

## What I did · Tech skills & stack

**The problem I solved:** B.Tech students face cumulative exams, internal-assessment backlogs and weak topics — but study plans are mostly static timetables, and generic AI advice doesn't know *their* real syllabus, deadlines, progress or weak spots.

**What I built:** Mentor Kit — an AI mentor that decides what a student should study next, and runs the whole loop:

scrape (real portal + Slack data) → plan (adaptive daily plan) → teach → quiz → revise.

**Tech I used / skills on this project:**
- **Python** — scraper, knowledge system, planner, teaching logic.
- **Playwright (Chromium)** — read-only capturer (no logins, no submissions, no uploads).
- **Daemon / automation** — background watch (hot + deep sweeps), change-diffing, launchd/cron scheduling.
- **LLM / AI** — Ollama (llama3.2:1b, qwen3:8b) + Open WebUI; mentor behavior via prompt (MENTOR.md), knowledge queries, adaptive depth, error tracking, quiz recall.
- **Export / docs** — question export → HTML/PDF (`export_html_pdf.py`).
- **Product assembly** — one repo tying scraper + data + AI mentor + study material + launcher.

**In plain words:** I connected real student data (college portal + Slack) to an AI mentor, so the AI — not the student — decides the next best study action, then teaches, quizzes and revises.

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
