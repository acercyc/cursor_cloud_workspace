#!/usr/bin/env python3
"""Download 5-minute intraday data for all S&P 500 tickers for a given date."""

from __future__ import annotations

import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf

from stock_analysis.sp500 import load_sp500_tickers

DATA_DIR = Path(__file__).resolve().parent / "data"


def download_intraday(
    tickers: list[str],
    date: str,
    interval: str = "5m",
    batch_size: int = 20,
) -> pd.DataFrame:
    """Download intraday data for a list of tickers on a single date.

    Parameters
    ----------
    tickers : list[str]
        Ticker symbols.
    date : str
        Target date in YYYY-MM-DD format.
    interval : str
        Bar interval (default "5m").
    batch_size : int
        How many tickers to request per yfinance call.

    Returns
    -------
    pd.DataFrame
        Combined DataFrame with a "Ticker" column.
    """
    target = datetime.strptime(date, "%Y-%m-%d")
    start = target.strftime("%Y-%m-%d")
    end = (target + timedelta(days=1)).strftime("%Y-%m-%d")

    all_frames = []
    total = len(tickers)

    for i in range(0, total, batch_size):
        batch = tickers[i : i + batch_size]
        batch_str = " ".join(batch)
        batch_num = i // batch_size + 1
        total_batches = (total + batch_size - 1) // batch_size
        print(f"  Batch {batch_num}/{total_batches}  ({len(batch)} tickers) ...", end=" ", flush=True)

        try:
            df = yf.download(
                batch_str,
                start=start,
                end=end,
                interval=interval,
                group_by="ticker",
                auto_adjust=False,
                progress=False,
            )
        except Exception as exc:
            print(f"ERROR: {exc}")
            continue

        if df.empty:
            print("no data")
            continue

        if len(batch) == 1:
            ticker = batch[0]
            chunk = df.copy()
            chunk["Ticker"] = ticker
            all_frames.append(chunk)
        else:
            for ticker in batch:
                try:
                    chunk = df[ticker].dropna(how="all").copy()
                    if not chunk.empty:
                        chunk["Ticker"] = ticker
                        all_frames.append(chunk)
                except KeyError:
                    pass

        count = sum(len(f) for f in all_frames)
        print(f"cumulative rows: {count}")
        time.sleep(0.3)

    if not all_frames:
        return pd.DataFrame()

    combined = pd.concat(all_frames)
    combined.index.name = "Datetime"
    if combined.index.tz is not None:
        combined.index = combined.index.tz_localize(None)
    cols = ["Ticker"] + [c for c in combined.columns if c != "Ticker"]
    return combined[cols]


def main() -> None:
    date = "2026-02-27"
    if len(sys.argv) > 1:
        date = sys.argv[1]

    print(f"Target date: {date}")
    print(f"Interval: 5m")
    print(f"Loading S&P 500 tickers...")
    tickers = load_sp500_tickers()
    print(f"Tickers: {len(tickers)}")
    print()

    print("Downloading 5-minute bars...")
    df = download_intraday(tickers, date=date, interval="5m")

    if df.empty:
        print("No data returned. The market may have been closed on that date.")
        return

    out_path = DATA_DIR / f"sp500_5min_{date}.csv"
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path)

    n_tickers = df["Ticker"].nunique()
    print(f"\nDone. {len(df)} rows across {n_tickers} tickers.")
    print(f"Saved to {out_path}")
    print(f"File size: {out_path.stat().st_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
