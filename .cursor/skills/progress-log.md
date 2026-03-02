# Skill: Progress Log

## When to use

Trigger this skill **every time you finish a big task**. A "big task" is one that produces meaningful, lasting changes to the repository (e.g., creating a new project, adding a major feature, building a new module).

Do NOT trigger for small things like minor follow-up tweaks, answering questions, or casual conversation.

## Procedure

1. Open (or create) the file `PROGRESS.md` at the repository root.
2. Append a new entry at the **bottom** of the log with the current date and the following three fields:

   - **Purpose** -- What the task set out to accomplish and why.
   - **Key files** -- The most important files created or changed (not every single file, just the highlights).
   - **Result** -- What was achieved, including any notable outcomes or numbers.

3. Keep each entry short (a few lines per field). This is a compressed summary, not a full report.

## Format

```markdown
### <short task title> — <YYYY-MM-DD>

**Purpose:** <one or two sentences>

**Key files:**
- `path/to/file1` -- brief note
- `path/to/file2` -- brief note

**Result:** <one or two sentences on the outcome>
```

## Example

```markdown
### U.S. Stock Analysis project — 2026-03-02

**Purpose:** Build a Python CLI for analyzing U.S. stocks with technical indicators and charting.

**Key files:**
- `us_stock_analysis/main.py` -- CLI entry point
- `us_stock_analysis/stock_analysis/analysis.py` -- returns, SMA, RSI, Bollinger, etc.
- `us_stock_analysis/stock_analysis/visualize.py` -- matplotlib chart generation

**Result:** Working CLI that fetches data from Yahoo Finance, prints summary stats, and saves PNG charts for any ticker.
```
