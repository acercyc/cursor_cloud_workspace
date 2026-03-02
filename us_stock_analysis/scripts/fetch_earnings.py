#!/usr/bin/env python3
"""Fetch upcoming S&P 500 earnings and save as CSV + Markdown.

Usage (run from the us_stock_analysis/ directory):
    python scripts/fetch_earnings.py
    python scripts/fetch_earnings.py --days 30
"""

from __future__ import annotations

import argparse
from datetime import date, timedelta

from stock_analysis.earnings import scan_earnings, save_earnings_csv, save_earnings_markdown


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch upcoming S&P 500 earnings.")
    parser.add_argument("--days", type=int, default=14, help="Days to look ahead (default: 14).")
    args = parser.parse_args()

    start = date.today()
    end = start + timedelta(days=args.days)

    print(f"Scanning S&P 500 earnings from {start} to {end}...")
    df = scan_earnings(start_date=start, end_date=end)

    if df.empty:
        print("No earnings found in that window.")
        return

    print(f"Found {len(df)} tickers.\n")

    csv_path = save_earnings_csv(df)
    md_path = save_earnings_markdown(df)

    print(f"CSV:      {csv_path}")
    print(f"Markdown: {md_path}")

    print(f"\n{'Ticker':<8} {'Date':<12} {'EPS Est':>10} {'Rev Est':>12}")
    print("-" * 44)
    for _, row in df.iterrows():
        eps = f"${row['EPS Est']:.2f}" if isinstance(row["EPS Est"], (int, float)) else ""
        rev = (
            f"${row['Rev Est'] / 1e9:.1f}B"
            if isinstance(row["Rev Est"], (int, float)) and row["Rev Est"]
            else ""
        )
        print(f"{row['Ticker']:<8} {str(row['Earnings Date']):<12} {eps:>10} {rev:>12}")


if __name__ == "__main__":
    main()
