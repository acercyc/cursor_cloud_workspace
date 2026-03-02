"""Fetch U.S. stock data from Yahoo Finance."""

from __future__ import annotations

from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf


def fetch_stock_data(
    ticker: str,
    period: str = "1y",
    start: str | None = None,
    end: str | None = None,
) -> pd.DataFrame:
    """Download OHLCV data for a single U.S. stock ticker.

    Parameters
    ----------
    ticker : str
        Stock symbol, e.g. "AAPL".
    period : str
        yfinance period string (e.g. "6mo", "1y", "5y"). Ignored when
        *start*/*end* are provided.
    start, end : str or None
        Date strings in "YYYY-MM-DD" format.

    Returns
    -------
    pd.DataFrame
        DataFrame indexed by Date with columns Open, High, Low, Close,
        Volume, and (when available) Adj Close.
    """
    stock = yf.Ticker(ticker)
    if start and end:
        df = stock.history(start=start, end=end, auto_adjust=False)
    else:
        df = stock.history(period=period, auto_adjust=False)

    if df.empty:
        raise ValueError(f"No data returned for ticker '{ticker}'.")

    df.index = pd.to_datetime(df.index)
    if df.index.tz is not None:
        df.index = df.index.tz_localize(None)
    return df


def fetch_info(ticker: str) -> dict:
    """Return the info dict for a ticker (company name, sector, etc.)."""
    return yf.Ticker(ticker).info
