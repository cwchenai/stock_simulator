"""Entry point demonstrating the backtracking system."""
from __future__ import annotations

from backtracking import Backtracker
from strategy import NaiveStrategy


def main() -> None:
    strategy = NaiveStrategy()
    backtracker = Backtracker(strategy)

    # Example usage in single stock mode
    history = [100.0, 101.5, 102.3]
    try:
        single_result = backtracker.single_stock_mode(history)
        print("Single stock result:\n", single_result)
    except Exception as exc:  # pragma: no cover - example run guard
        print("Single stock mode failed:", exc)

    # Example usage in market mode
    histories = {
        "AAPL": [150.0, 151.2, 152.3],
        "GOOG": [2700.0, 2710.5, 2699.0],
        "MSFT": [299.0, 300.5, 305.0],
    }
    try:
        market_result = backtracker.market_mode(histories)
        print("Market mode result:\n", market_result)
    except Exception as exc:  # pragma: no cover - example run guard
        print("Market mode failed:", exc)


if __name__ == "__main__":  # pragma: no cover - script execution
    main()
