#!/usr/bin/env python3
"""U.S. Stock Analysis CLI.

Usage examples:
    python main.py AAPL
    python main.py MSFT GOOGL --period 6mo
    python main.py TSLA --start 2024-01-01 --end 2025-01-01
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tabulate import tabulate

from stock_analysis.fetcher import fetch_stock_data, fetch_info
from stock_analysis.analysis import summary_stats
from stock_analysis.visualize import (
    plot_price_with_ma,
    plot_bollinger,
    plot_rsi,
    plot_volume,
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze U.S. stocks: summary stats, moving averages, "
        "Bollinger Bands, RSI, and volume charts."
    )
    parser.add_argument(
        "tickers",
        nargs="+",
        help="One or more stock ticker symbols (e.g. AAPL MSFT GOOGL).",
    )
    parser.add_argument(
        "--period",
        default="1y",
        help="Data period (default: 1y). Ignored when --start/--end are set.",
    )
    parser.add_argument("--start", default=None, help="Start date (YYYY-MM-DD).")
    parser.add_argument("--end", default=None, help="End date (YYYY-MM-DD).")
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory for chart PNGs (default: output/).",
    )
    parser.add_argument(
        "--no-charts",
        action="store_true",
        help="Skip chart generation, only print summary stats.",
    )
    return parser.parse_args(argv)


def analyze_ticker(
    ticker: str,
    period: str,
    start: str | None,
    end: str | None,
    output_dir: Path,
    generate_charts: bool,
) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {ticker}")
    print(f"{'=' * 60}")

    try:
        info = fetch_info(ticker)
        name = info.get("shortName") or info.get("longName", ticker)
        sector = info.get("sector", "N/A")
        industry = info.get("industry", "N/A")
        print(f"  Company : {name}")
        print(f"  Sector  : {sector}")
        print(f"  Industry: {industry}")
    except Exception:
        print(f"  (Could not fetch company info for {ticker})")

    df = fetch_stock_data(ticker, period=period, start=start, end=end)
    print(f"  Data points: {len(df)}  ({df.index[0].date()} to {df.index[-1].date()})")

    stats = summary_stats(df)
    print()
    print(tabulate(stats.items(), headers=["Metric", "Value"], tablefmt="simple"))

    if generate_charts:
        ticker_dir = output_dir / ticker
        ticker_dir.mkdir(parents=True, exist_ok=True)

        plot_price_with_ma(df, ticker, save_path=ticker_dir / "price_ma.png")
        plot_bollinger(df, ticker, save_path=ticker_dir / "bollinger.png")
        plot_rsi(df, ticker, save_path=ticker_dir / "rsi.png")
        plot_volume(df, ticker, save_path=ticker_dir / "volume.png")
        print(f"\n  Charts saved to {ticker_dir}/")


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    output_dir = Path(args.output_dir)
    generate_charts = not args.no_charts

    for ticker in args.tickers:
        try:
            analyze_ticker(
                ticker.upper(),
                period=args.period,
                start=args.start,
                end=args.end,
                output_dir=output_dir,
                generate_charts=generate_charts,
            )
        except Exception as exc:
            print(f"\n  ERROR analyzing {ticker}: {exc}", file=sys.stderr)

    print()


if __name__ == "__main__":
    main()
