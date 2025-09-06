"""Prompt generation utilities for strategies."""
from typing import Dict, Sequence


def single_stock_prompt(history: Sequence[float]) -> str:
    """Return a prompt for analyzing a single stock history."""
    return (
        "You are a trading assistant. Given the following price history "
        f"{list(history)}, provide a short analysis and next action."
    )


def market_prompt(histories: Dict[str, Sequence[float]]) -> str:
    """Return a prompt for analyzing multiple stock histories."""
    lines = ["You are a trading assistant. Analyze these stocks:"]
    for ticker, prices in histories.items():
        lines.append(f"- {ticker}: {list(prices)}")
    lines.append("Provide a concise analysis of the market.")
    return "\n".join(lines)
