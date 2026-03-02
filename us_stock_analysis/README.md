# U.S. Stock Analysis

## Purpose
Python toolkit for analyzing U.S. stocks. Fetches live market data, computes technical indicators, generates charts, and supports batch analysis of S&P 500 constituents.

## Usage
```bash
cd us_stock_analysis
source .venv/bin/activate

# Analyze individual tickers
python main.py AAPL MSFT --period 6mo

# Refresh S&P 500 ticker list from Wikipedia
python -m stock_analysis.sp500

# Download 5-minute intraday data for all S&P 500 tickers
python download_sp500_intraday.py 2026-02-27

# Run the sector analysis notebook
jupyter notebook sector_analysis.ipynb
```

## Key files
- `main.py` -- CLI entry point for single/multi-ticker analysis with charts
- `stock_analysis/fetcher.py` -- Yahoo Finance data fetching via yfinance
- `stock_analysis/analysis.py` -- Technical indicators (SMA, EMA, Bollinger, RSI, volatility, Sharpe, drawdown)
- `stock_analysis/visualize.py` -- Matplotlib chart generation (price+MA, Bollinger, RSI, volume)
- `stock_analysis/sp500.py` -- Fetch and cache S&P 500 constituent list from Wikipedia
- `download_sp500_intraday.py` -- Batch download 5-min intraday bars for all S&P 500 tickers
- `sector_analysis.ipynb` -- Jupyter notebook: sector-level intraday analysis with 6 chart types
- `data/sp500_tickers.txt` -- Cached ticker list (one per line)
- `data/sp500_constituents.csv` -- Full S&P 500 table (symbol, company, sector, industry, etc.)
- `data/sp500_5min_*.csv` -- Downloaded intraday data files
- `data/upcoming_earnings_*.csv` -- Earnings calendar snapshots
