"""Fetch and cache stock universe lists (S&P 500, etc.) from Wikipedia."""

from __future__ import annotations

import csv
from io import StringIO
from pathlib import Path

import pandas as pd
import requests

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "reference"
SP500_CSV = DATA_DIR / "sp500_constituents.csv"
SP500_TICKERS_TXT = DATA_DIR / "sp500_tickers.txt"

WIKI_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"


def fetch_sp500_table() -> pd.DataFrame:
    """Scrape the current S&P 500 table from Wikipedia and return a DataFrame."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; StockAnalysis/1.0)"}
    resp = requests.get(WIKI_URL, headers=headers, timeout=15)
    resp.raise_for_status()
    tables = pd.read_html(StringIO(resp.text))
    return tables[0]


def save_sp500(df: pd.DataFrame | None = None) -> Path:
    """Fetch (if needed) and save the S&P 500 list to data/reference/sp500_constituents.csv
    and data/reference/sp500_tickers.txt. Returns the CSV path."""
    if df is None:
        df = fetch_sp500_table()

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    df.to_csv(SP500_CSV, index=False, quoting=csv.QUOTE_ALL)

    tickers = sorted(df["Symbol"].str.strip().tolist())
    SP500_TICKERS_TXT.write_text("\n".join(tickers) + "\n")

    return SP500_CSV


def load_sp500_tickers() -> list[str]:
    """Load tickers from the cached text file, fetching first if missing."""
    if not SP500_TICKERS_TXT.exists():
        save_sp500()
    return [t.strip() for t in SP500_TICKERS_TXT.read_text().splitlines() if t.strip()]


def load_sp500_sector_map() -> dict[str, str]:
    """Return a dict mapping ticker -> GICS Sector from the cached CSV."""
    if not SP500_CSV.exists():
        save_sp500()
    df = pd.read_csv(SP500_CSV)
    return df.set_index("Symbol")["GICS Sector"].to_dict()


def load_sp500_name_map() -> dict[str, str]:
    """Return a dict mapping ticker -> company name from the cached CSV."""
    if not SP500_CSV.exists():
        save_sp500()
    df = pd.read_csv(SP500_CSV)
    return df.set_index("Symbol")["Security"].to_dict()


if __name__ == "__main__":
    print("Fetching S&P 500 constituents from Wikipedia...")
    df = fetch_sp500_table()
    path = save_sp500(df)
    tickers = load_sp500_tickers()
    print(f"Saved {len(df)} entries to {path}")
    print(f"Saved {len(tickers)} tickers to {SP500_TICKERS_TXT}")
    print(f"First 10: {tickers[:10]}")
    print(f"Last  10: {tickers[-10:]}")
