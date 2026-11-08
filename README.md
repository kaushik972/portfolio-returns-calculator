# Portfolio Returns Calculator

Takes monthly prices for a few assets and works out how an equal-weight portfolio would have performed: total return, CAGR, and maximum drawdown.

## Why I built this

After about 7 years of trading on my own, I wanted to understand my results like an analyst would — not just "up or down", but annualised return (CAGR) and worst peak-to-trough fall (drawdown). This project practises the maths in plain Python, with no libraries, so I understand every step.

## What it does

- Reads `prices.csv`: monthly closing prices for 3 ETFs (Nikkei, S&P 500, gold), Jan 2023 – Dec 2024
- Builds an equal-weight portfolio (rebalanced monthly — the portfolio's monthly return is the average of the assets' returns)
- Reports total return, CAGR, and max drawdown, starting from a value of 100
- Also prints each asset's own total return for comparison

## How to run

```bash
cd portfolio-returns-calculator
python portfolio_returns.py
```

Swap in your own assets by editing `prices.csv` (keep the format: `date` first, then one column per asset).

## Sample output

```
Period: 2023-01-31 to 2024-12-31 (1.92 years, monthly data)
Assets (equal weight): nikkei_etf, sp500_etf, gold_etf
--------------------------------------------------------
Start value:            100.00
End value:              144.15
Total return:           44.15%
CAGR (per year):        21.02%
Max drawdown:           -3.24%
--------------------------------------------------------
Each asset on its own (total return):
  nikkei_etf     47.20%
  sp500_etf      39.19%
  gold_etf       43.41%
```

Interesting bit: the portfolio's worst drawdown (-3.24%) is small because the three assets don't all fall at the same time — that's diversification doing its job. (Prices are sample data for practice, not live market data.)

## Files

- `portfolio_returns.py` — the program
- `prices.csv` — 24 months of sample prices for 3 assets

## Next steps

- Try different weights (e.g. 50/30/20) and compare drawdowns
- Add volatility (standard deviation of monthly returns)
- Use daily prices downloaded from a real data source

*Standard library only. Built while learning Python.*
