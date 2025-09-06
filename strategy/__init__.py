"""Strategy package exposing interfaces and implementations."""

from .interface import Strategy
from .naive import NaiveStrategy

__all__ = ["Strategy", "NaiveStrategy"]
