# Progress Log

### U.S. Stock Analysis project — 2026-03-02

**Purpose:** Build a Python CLI for analyzing U.S. stocks with technical indicators (SMA, EMA, Bollinger Bands, RSI) and chart generation.

**Key files:**
- `us_stock_analysis/main.py` -- CLI entry point accepting tickers, period, date range
- `us_stock_analysis/stock_analysis/analysis.py` -- returns, moving averages, RSI, volatility, summary stats
- `us_stock_analysis/stock_analysis/visualize.py` -- matplotlib charts (price+MA, Bollinger, RSI, volume)

**Result:** Working CLI that fetches live data from Yahoo Finance, prints summary stats (total return, Sharpe, max drawdown), and saves PNG charts per ticker.

---

### S&P 500 ticker list — 2026-03-02

**Purpose:** Fetch and store the full list of S&P 500 constituents for use in batch analysis.

**Key files:**
- `us_stock_analysis/stock_analysis/sp500.py` -- fetches table from Wikipedia, saves/loads cached files
- `us_stock_analysis/data/sp500_constituents.csv` -- full table (symbol, company, sector, industry, etc.)
- `us_stock_analysis/data/sp500_tickers.txt` -- one ticker per line, sorted

**Result:** 503 tickers saved. Can be loaded programmatically via `load_sp500_tickers()` or refreshed with `python -m stock_analysis.sp500`.
