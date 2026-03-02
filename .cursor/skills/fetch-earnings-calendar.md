# Skill: Fetch S&P 500 Earnings Calendar

## When to use

Use this skill when the user asks for upcoming earnings reports, earnings dates, or earnings calendars for S&P 500 stocks. This covers requests like "which stocks report earnings this week," "find earnings in the next N days," or "get the earnings calendar."

## Prerequisites

- Python venv at `us_stock_analysis/.venv` with `yfinance` and `pandas` installed.
- S&P 500 ticker list at `us_stock_analysis/data/sp500_tickers.txt` (one ticker per line). If missing, regenerate it by running `python -m stock_analysis.sp500` from the `us_stock_analysis/` directory.

## Procedure

### Step 1: Determine the date range

- Default: today through 14 calendar days from today.
- If the user specifies a different window (e.g., "this week," "next 30 days"), adjust accordingly.

### Step 2: Run a programmatic scan with yfinance

Use the script pattern below. Key details that prevent common bugs:

1. **Dot-notation tickers:** S&P 500 uses dots (e.g., `BF.B`, `BRK.B`) but yfinance expects hyphens (`BF-B`, `BRK-B`). Always `.replace('.', '-')` before querying, and map back to the original symbol for output.
2. **Date types:** `yf.Ticker(symbol).calendar['Earnings Date']` returns a list of `datetime.date` objects (not `datetime.datetime`). Compare using `datetime.date`, not `datetime.datetime`.
3. **Calendar structure:** The `.calendar` property returns a dict (or `None`). The `Earnings Date` key holds a `list[datetime.date]`. Other useful keys: `Earnings Average` (EPS estimate), `Revenue Average` (revenue estimate).
4. **Rate limiting:** yfinance hits Yahoo Finance's API. Process tickers sequentially (no threading needed, it's fast enough). No explicit sleep is required for ~500 tickers.

```python
import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import warnings
warnings.filterwarnings('ignore')

# Load tickers
tickers_raw = [t.strip() for t in open('data/sp500_tickers.txt') if t.strip()]
tickers_yf = [t.replace('.', '-') for t in tickers_raw]
ticker_map = dict(zip(tickers_yf, tickers_raw))

start_date = date.today()
end_date = start_date + timedelta(days=14)

results = []
for ticker in tickers_yf:
    try:
        cal = yf.Ticker(ticker).calendar
        if cal and isinstance(cal, dict) and 'Earnings Date' in cal:
            for d in cal['Earnings Date']:
                if isinstance(d, date) and start_date <= d <= end_date:
                    results.append({
                        'Ticker': ticker_map.get(ticker, ticker),
                        'Earnings Date': d,
                        'EPS Est': cal.get('Earnings Average', ''),
                        'Rev Est': cal.get('Revenue Average', ''),
                    })
                    break
    except Exception:
        pass

df = pd.DataFrame(results).sort_values('Earnings Date')
```

### Step 3: Format and present

- Sort by Earnings Date ascending.
- Format revenue as `$X.XB` and EPS as `$X.XX`.
- Present as a markdown table to the user.
- Save the result to `us_stock_analysis/data/upcoming_earnings_<start>_<end>.csv`.

### Step 4: Enrich with web search (optional)

If the user wants more context (expected themes, market impact, which reports are most important), do a web search for the reporting week to find analyst previews. This is supplementary, not required.

## Common pitfalls

| Pitfall | Fix |
|---|---|
| 0 results because of `datetime` vs `date` | Always compare with `datetime.date`, not `datetime.datetime` |
| `BF.B` / `BRK.B` return no data | Replace dots with hyphens for yfinance queries |
| `.calendar` returns `None` | Some tickers have no scheduled earnings yet; skip with `try/except` |
| Ticker not in S&P 500 but found via web search | Cross-check against `sp500_tickers.txt` before including |
