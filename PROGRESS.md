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

---

### S&P 500 5-minute intraday download — 2026-03-02

**Purpose:** Download 5-minute resolution intraday bars for all S&P 500 stocks for a given trading day.

**Key files:**
- `us_stock_analysis/download_sp500_intraday.py` -- batch download script (batches of 20 tickers via yfinance)
- `us_stock_analysis/data/sp500_5min_2026-02-27.csv` -- 39,035 rows across 501 tickers (4.5 MB)

**Result:** Successfully downloaded Friday 2026-02-27 data. 78 bars per ticker (full 9:30am-4pm session in 5-min intervals). Only BF.B and BRK.B failed (dot-notation ticker issue in yfinance).
