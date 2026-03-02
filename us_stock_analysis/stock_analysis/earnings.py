"""Fetch upcoming earnings dates for a list of tickers via yfinance."""

from __future__ import annotations

import csv
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf

from .universe import load_sp500_tickers, load_sp500_name_map, load_sp500_sector_map

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "earnings"


def scan_earnings(
    tickers: list[str] | None = None,
    start_date: date | None = None,
    end_date: date | None = None,
    days_ahead: int = 14,
) -> pd.DataFrame:
    """Scan tickers for upcoming earnings dates.

    Parameters
    ----------
    tickers : list[str] or None
        Tickers to scan. Defaults to S&P 500.
    start_date : date or None
        Start of window. Defaults to today.
    end_date : date or None
        End of window. Defaults to start_date + days_ahead.
    days_ahead : int
        Number of days to look ahead (used when end_date is None).

    Returns
    -------
    pd.DataFrame
        Sorted by Earnings Date with columns: Ticker, Earnings Date,
        EPS Est, Rev Est.
    """
    if tickers is None:
        raw_tickers = load_sp500_tickers()
    else:
        raw_tickers = tickers

    tickers_yf = [t.replace(".", "-") for t in raw_tickers]
    ticker_map = dict(zip(tickers_yf, raw_tickers))

    if start_date is None:
        start_date = date.today()
    if end_date is None:
        end_date = start_date + timedelta(days=days_ahead)

    results = []
    for ticker in tickers_yf:
        try:
            cal = yf.Ticker(ticker).calendar
            if cal and isinstance(cal, dict) and "Earnings Date" in cal:
                for d in cal["Earnings Date"]:
                    if isinstance(d, date) and start_date <= d <= end_date:
                        results.append(
                            {
                                "Ticker": ticker_map.get(ticker, ticker),
                                "Earnings Date": d,
                                "EPS Est": cal.get("Earnings Average", ""),
                                "Rev Est": cal.get("Revenue Average", ""),
                            }
                        )
                        break
        except Exception:
            pass

    df = pd.DataFrame(results)
    if not df.empty:
        df = df.sort_values("Earnings Date").reset_index(drop=True)
    return df


def save_earnings_csv(df: pd.DataFrame, filename: str | None = None) -> Path:
    """Save earnings DataFrame to data/earnings/ as CSV."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if filename is None:
        if not df.empty:
            start = df["Earnings Date"].min()
            end = df["Earnings Date"].max()
            filename = f"upcoming_earnings_{start}_{end}.csv"
        else:
            filename = "upcoming_earnings.csv"

    df_out = df.copy()
    if "Rev Est" in df_out.columns:
        df_out["Rev Est ($B)"] = df_out["Rev Est"].apply(
            lambda x: f"${x / 1e9:.1f}B" if isinstance(x, (int, float)) and x else ""
        )
        df_out["EPS Est"] = df_out["EPS Est"].apply(
            lambda x: f"${x:.2f}" if isinstance(x, (int, float)) else ""
        )
        df_out = df_out[["Ticker", "Earnings Date", "EPS Est", "Rev Est ($B)"]]

    path = DATA_DIR / filename
    df_out.to_csv(path, index=False)
    return path


def save_earnings_markdown(df: pd.DataFrame, filename: str = "earnings_calendar.md") -> Path:
    """Save earnings DataFrame as a readable markdown file."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    name_map = load_sp500_name_map()
    sector_map = load_sp500_sector_map()

    lines = [
        "# S&P 500 Earnings Calendar",
        "",
    ]

    if not df.empty:
        start = df["Earnings Date"].min()
        end = df["Earnings Date"].max()
        lines.append(f"## {start.strftime('%B %d')} - {end.strftime('%B %d, %Y')}")
        lines.append("")
        lines.append(f"**{len(df)} S&P 500 companies** reporting earnings in this window.")
    else:
        lines.append("No upcoming earnings found.")

    lines.append("")
    lines.append(f"*Data sourced from Yahoo Finance via yfinance.*")
    lines.append("")

    current_date = None
    for _, row in df.iterrows():
        d = row["Earnings Date"]
        if d != current_date:
            current_date = d
            dt = pd.Timestamp(d)
            lines.append(f"### {dt.strftime('%A, %B %d, %Y')}")
            lines.append("")
            lines.append("| Ticker | Company | Sector | EPS Est | Rev Est |")
            lines.append("|--------|---------|--------|---------|---------|")

        ticker = row["Ticker"]
        company = name_map.get(ticker, "")
        sector = sector_map.get(ticker, "")
        eps = f"${row['EPS Est']:.2f}" if isinstance(row["EPS Est"], (int, float)) else ""
        rev = (
            f"${row['Rev Est'] / 1e9:.1f}B"
            if isinstance(row["Rev Est"], (int, float)) and row["Rev Est"]
            else ""
        )
        lines.append(f"| **{ticker}** | {company} | {sector} | {eps} | {rev} |")

    lines.append("")

    path = DATA_DIR / filename
    path.write_text("\n".join(lines) + "\n")
    return path
