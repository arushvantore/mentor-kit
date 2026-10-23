#!/bin/sh
# Mentor background tracker — permanent watch daemon.
# Captures every URL in targets.txt every 120s into materials/live_*.md
# (current) and materials/archive_YYYYMMDD_*.md (daily history).
# Read-only: never types, never submits.
cd "$(dirname "$0")" || exit 1
exec .venv/bin/python scrape.py --watch --interval 120
