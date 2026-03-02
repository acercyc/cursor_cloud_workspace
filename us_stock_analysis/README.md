# U.S. Stock Analysis

## Purpose
Python toolkit for analyzing U.S. stocks. Fetches live market data, computes technical indicators, generates charts, and supports batch analysis of S&P 500 constituents.

## Usage
```bash
cd us_stock_analysis
source .venv/bin/activate

# Analyze individual tickers (charts saved to output/tickers/<TICKER>/)
python scripts/analyze_tickers.py AAPL MSFT --period 6mo

# Refresh S&P 500 ticker list from Wikipedia
python -m stock_analysis.universe

# Download 5-minute intraday data for all S&P 500 tickers
python scripts/download_intraday.py 2026-02-27

# Fetch upcoming earnings calendar (CSV + Markdown)
python scripts/fetch_earnings.py --days 14

# Run the sector analysis notebook
jupyter notebook notebooks/sector_analysis.ipynb
```

## Project structure
```
us_stock_analysis/
├── stock_analysis/              # Core library
│   ├── universe.py              #   S&P 500 list, sector/name maps
│   ├── fetcher.py               #   Yahoo Finance data fetching
│   ├── earnings.py              #   Earnings calendar scanning
│   ├── analysis.py              #   Technical indicators and stats
│   └── visualize.py             #   Chart generation (matplotlib)
│
├── scripts/                     # CLI entry points
│   ├── analyze_tickers.py       #   Single/multi-ticker analysis
│   ├── download_intraday.py     #   Batch intraday data download
│   └── fetch_earnings.py        #   Earnings calendar fetch
│
├── notebooks/                   # Jupyter notebooks
│   └── sector_analysis.ipynb    #   Sector-level intraday analysis
│
├── data/                        # All data files
│   ├── reference/               #   Slowly-changing reference data
│   │   ├── sp500_tickers.txt
│   │   └── sp500_constituents.csv
│   ├── market/                  #   Downloaded price/volume data
│   │   └── sp500_5min_*.csv
│   └── earnings/                #   Earnings calendar snapshots
│       ├── earnings_calendar.md
│       └── upcoming_earnings_*.csv
│
├── output/                      # Generated charts
│   ├── tickers/                 #   Per-ticker charts (AAPL/, MSFT/, ...)
│   └── sector/                  #   Sector-level charts
│
├── requirements.txt
└── README.md
```
