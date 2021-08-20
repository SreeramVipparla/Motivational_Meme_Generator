"""This module for ingestors is responsible for parsing files."""
from .QuoteModel import QuoteModel
from abc import ABC, abstractmethod
from typing import List


class IngestorInterface(ABC):
    """Abstract class with class and abstract method."""

    Extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
      ext = path.split('.')[-1]
      return ext in cls.Extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
