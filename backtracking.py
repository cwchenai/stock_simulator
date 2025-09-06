"""Simple backtracking system supporting single stock and market modes."""
from __future__ import annotations

from typing import Dict, Sequence

from strategy.interface import Strategy


class Backtracker:
    """Orchestrate backtracking using a given strategy."""

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def single_stock_mode(self, history: Sequence[float]) -> str:
        """Backtrack in single-stock mode using ``history``."""
        return self.strategy.single_stock(history)

    def market_mode(self, histories: Dict[str, Sequence[float]]) -> str:
        """Backtrack in market mode for selected targets."""
        targets = self.strategy.get_targets()
        subset = {t: histories[t] for t in targets if t in histories}
        return self.strategy.market(subset)
