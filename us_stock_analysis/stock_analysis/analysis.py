"""Core stock analysis functions: returns, moving averages, volatility."""

from __future__ import annotations

import numpy as np
import pandas as pd


def daily_returns(df: pd.DataFrame, column: str = "Close") -> pd.Series:
    """Compute daily percentage returns."""
    return df[column].pct_change().dropna()


def cumulative_returns(df: pd.DataFrame, column: str = "Close") -> pd.Series:
    """Compute cumulative returns starting from 1.0."""
    returns = daily_returns(df, column)
    return (1 + returns).cumprod()


def moving_average(
    df: pd.DataFrame, window: int = 50, column: str = "Close"
) -> pd.Series:
    """Simple Moving Average (SMA)."""
    return df[column].rolling(window=window).mean()


def exponential_moving_average(
    df: pd.DataFrame, span: int = 20, column: str = "Close"
) -> pd.Series:
    """Exponential Moving Average (EMA)."""
    return df[column].ewm(span=span, adjust=False).mean()


def bollinger_bands(
    df: pd.DataFrame, window: int = 20, num_std: float = 2.0, column: str = "Close"
) -> pd.DataFrame:
    """Compute Bollinger Bands (middle, upper, lower)."""
    sma = df[column].rolling(window=window).mean()
    std = df[column].rolling(window=window).std()
    return pd.DataFrame(
        {
            "BB_Middle": sma,
            "BB_Upper": sma + num_std * std,
            "BB_Lower": sma - num_std * std,
        },
        index=df.index,
    )


def annualized_volatility(
    df: pd.DataFrame, window: int = 252, column: str = "Close"
) -> pd.Series:
    """Rolling annualized volatility (standard deviation of returns * sqrt(252))."""
    returns = daily_returns(df, column)
    return returns.rolling(window=window).std() * np.sqrt(252)


def rsi(df: pd.DataFrame, period: int = 14, column: str = "Close") -> pd.Series:
    """Relative Strength Index (RSI)."""
    delta = df[column].diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def summary_stats(df: pd.DataFrame, column: str = "Close") -> dict:
    """Return a summary dict: total return, annualized return, volatility, Sharpe, max drawdown."""
    prices = df[column].dropna()
    if len(prices) < 2:
        return {}

    total_return = (prices.iloc[-1] / prices.iloc[0]) - 1
    n_days = (prices.index[-1] - prices.index[0]).days
    ann_return = (1 + total_return) ** (365.0 / max(n_days, 1)) - 1

    returns = prices.pct_change().dropna()
    vol = returns.std() * np.sqrt(252)
    sharpe = ann_return / vol if vol != 0 else 0.0

    cum_max = prices.cummax()
    drawdown = (prices - cum_max) / cum_max
    max_dd = drawdown.min()

    return {
        "Start Date": str(prices.index[0].date()),
        "End Date": str(prices.index[-1].date()),
        "Total Return": f"{total_return:.2%}",
        "Annualized Return": f"{ann_return:.2%}",
        "Annualized Volatility": f"{vol:.2%}",
        "Sharpe Ratio (rfr=0)": f"{sharpe:.2f}",
        "Max Drawdown": f"{max_dd:.2%}",
    }
