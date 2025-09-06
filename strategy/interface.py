"""Strategy interface for stock backtracking systems."""
from abc import ABC, abstractmethod
from typing import Dict, List, Sequence


class Strategy(ABC):
    """Abstract base class for trading strategies."""

    @property
    @abstractmethod
    def target_change_frequency(self) -> int:
        """Number of iterations before target list should be refreshed."""

    @abstractmethod
    def get_targets(self) -> Sequence[str]:
        """Return a sequence of stock tickers to track in market mode."""

    @abstractmethod
    def single_stock(self, history: Sequence[float]) -> str:
        """Analyze history for a single stock."""

    @abstractmethod
    def market(self, histories: Dict[str, Sequence[float]]) -> str:
        """Analyze histories for multiple stocks."""
