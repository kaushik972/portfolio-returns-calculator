"""
Portfolio Returns Calculator
----------------------------
Reads monthly prices for a few assets from prices.csv and builds an
equal-weight portfolio (same money in each asset, rebalanced every
month). It then reports:

  * Total return over the whole period
  * CAGR  (compound annual growth rate - the smooth yearly rate)
  * Maximum drawdown (the worst peak-to-trough fall)

It also prints each asset's own total return for comparison.

Built by Kaushik Shivam while learning Python.
Standard library only (csv, datetime).
"""

import csv
from datetime import date

PRICES_FILE = "prices.csv"
START_VALUE = 100.0  # imagine starting with 100 units of money


def load_prices(filename):
    """Return (list of dates, {asset: [prices...]})."""
    dates = []
    assets = {}
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dates.append(date.fromisoformat(row["date"]))
            for name in reader.fieldnames:
                if name == "date":
                    continue
                assets.setdefault(name, []).append(float(row[name]))
    return dates, assets


def portfolio_values(assets):
    """Grow START_VALUE in an equal-weight, monthly-rebalanced portfolio.

    Each month, every asset holds the same share of the portfolio, so
    the portfolio's monthly return is simply the average of the
    assets' monthly returns.
    """
    values = [START_VALUE]
    n_months = len(next(iter(assets.values())))
    for i in range(1, n_months):
        monthly_returns = []
        for prices in assets.values():
            monthly_returns.append(prices[i] / prices[i - 1] - 1)
        avg_return = sum(monthly_returns) / len(monthly_returns)
        values.append(values[-1] * (1 + avg_return))
    return values


def max_drawdown(values):
    """Largest fall from a previous peak, as a negative fraction."""
    peak = values[0]
    worst = 0.0
    for v in values:
        peak = max(peak, v)
        drawdown = v / peak - 1
        worst = min(worst, drawdown)
    return worst


def main():
    dates, assets = load_prices(PRICES_FILE)
    values = portfolio_values(assets)

    years = (dates[-1] - dates[0]).days / 365.25
    total_return = values[-1] / values[0] - 1
    cagr = (values[-1] / values[0]) ** (1 / years) - 1
    drawdown = max_drawdown(values)

    print(f"Period: {dates[0]} to {dates[-1]} ({years:.2f} years, monthly data)")
    print(f"Assets (equal weight): {', '.join(assets)}")
    print("-" * 56)
    print(f"Start value:        {values[0]:>10.2f}")
    print(f"End value:          {values[-1]:>10.2f}")
    print(f"Total return:       {total_return:>10.2%}")
    print(f"CAGR (per year):    {cagr:>10.2%}")
    print(f"Max drawdown:       {drawdown:>10.2%}")
    print("-" * 56)
    print("Each asset on its own (total return):")
    for name, prices in assets.items():
        print(f"  {name:<12} {prices[-1] / prices[0] - 1:>8.2%}")


if __name__ == "__main__":
    main()
