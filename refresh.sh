#!/bin/sh
# Daily capture refresh: re-reads every URL in targets.txt, headless.
# Safe: read-only. Session expired -> captures.log says ACTION NEEDED.
cd "$(dirname "$0")" || exit 1
exec .venv/bin/python scrape.py --auto "$@"
