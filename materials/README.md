# Drop study material HERE

Two ways material arrives:

1. **Automatic (daily)** — `python3 scrape.py --auto` saves the newest
   content of every URL in `../targets.txt` as `auto_YYYYMMDD_*.md`
   (+ full-page `.png`). Same-day re-runs overwrite, so this folder
   stays tidy.

2. **Manual interactive** — `python3 scrape.py <url>` opens a window;
   you browse (deep history, old quizzes, long Slack threads) and click
   the blue CAPTURE button on each page. Files get timestamped names.

The AI reads every `.md` here (and its `.png` screenshot) directly from
this Mac. PDFs, screenshots you take yourself, or plain-text notes you
paste into files also belong here.

NEVER put passwords, tokens, or login files in this folder.
