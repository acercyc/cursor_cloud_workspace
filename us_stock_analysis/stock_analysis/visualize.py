"""Charting helpers for stock analysis (matplotlib, saved to PNG)."""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

from . import analysis


def _style_ax(ax: plt.Axes) -> None:
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if labels:
        ax.legend(fontsize=8)
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right", fontsize=8)


def plot_price_with_ma(
    df: pd.DataFrame,
    ticker: str,
    ma_windows: tuple[int, ...] = (20, 50, 200),
    save_path: str | Path | None = None,
) -> None:
    """Price chart with simple moving averages."""
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df["Close"], label="Close", linewidth=1.2)
    for w in ma_windows:
        sma = analysis.moving_average(df, window=w)
        ax.plot(df.index, sma, label=f"SMA-{w}", linewidth=0.9, linestyle="--")
    ax.set_title(f"{ticker} Price & Moving Averages")
    ax.set_ylabel("Price (USD)")
    _style_ax(ax)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    plt.close(fig)


def plot_bollinger(
    df: pd.DataFrame,
    ticker: str,
    window: int = 20,
    save_path: str | Path | None = None,
) -> None:
    """Bollinger Bands chart."""
    bb = analysis.bollinger_bands(df, window=window)
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df["Close"], label="Close", linewidth=1.2)
    ax.plot(df.index, bb["BB_Middle"], label="Middle", linewidth=0.8, linestyle="--")
    ax.fill_between(
        df.index, bb["BB_Upper"], bb["BB_Lower"], alpha=0.15, label="Band"
    )
    ax.set_title(f"{ticker} Bollinger Bands ({window})")
    ax.set_ylabel("Price (USD)")
    _style_ax(ax)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    plt.close(fig)


def plot_rsi(
    df: pd.DataFrame,
    ticker: str,
    period: int = 14,
    save_path: str | Path | None = None,
) -> None:
    """RSI chart with overbought/oversold bands."""
    rsi_vals = analysis.rsi(df, period=period)
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.plot(df.index, rsi_vals, label=f"RSI-{period}", linewidth=1.0, color="purple")
    ax.axhline(70, color="red", linewidth=0.7, linestyle="--", label="Overbought (70)")
    ax.axhline(30, color="green", linewidth=0.7, linestyle="--", label="Oversold (30)")
    ax.set_ylim(0, 100)
    ax.set_title(f"{ticker} RSI ({period})")
    _style_ax(ax)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    plt.close(fig)


def plot_volume(
    df: pd.DataFrame,
    ticker: str,
    save_path: str | Path | None = None,
) -> None:
    """Volume bar chart."""
    fig, ax = plt.subplots(figsize=(12, 3))
    colors = [
        "green" if c >= o else "red"
        for c, o in zip(df["Close"], df["Open"])
    ]
    ax.bar(df.index, df["Volume"], color=colors, width=0.8, alpha=0.7)
    ax.set_title(f"{ticker} Volume")
    ax.set_ylabel("Volume")
    _style_ax(ax)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    plt.close(fig)
