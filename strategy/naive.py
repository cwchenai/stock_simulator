"""Naive strategy that queries the OpenAI API."""
from __future__ import annotations

from typing import Dict, Sequence

from .interface import Strategy
from . import prompt
from .openai_api import ask_openai


class NaiveStrategy(Strategy):
    """Very naive strategy that simply forwards prompts to OpenAI."""

    def __init__(self, target_change_frequency: int = 5) -> None:
        self._freq = target_change_frequency
        self._targets: Sequence[str] = ("AAPL", "GOOG", "MSFT")

    # ------------------------------------------------------------------
    @property
    def target_change_frequency(self) -> int:  # pragma: no cover - simple getter
        return self._freq

    # ------------------------------------------------------------------
    def get_targets(self) -> Sequence[str]:
        return self._targets

    # ------------------------------------------------------------------
    def single_stock(self, history: Sequence[float]) -> str:
        p = prompt.single_stock_prompt(history)
        return ask_openai(p)

    # ------------------------------------------------------------------
    def market(self, histories: Dict[str, Sequence[float]]) -> str:
        p = prompt.market_prompt(histories)
        return ask_openai(p)
