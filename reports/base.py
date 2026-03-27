from abc import ABC, abstractmethod
from typing import List, Dict


class BaseReport(ABC):
    name: str

    @abstractmethod
    def build(self, rows: List[Dict]) -> List[List]:
        pass

    @abstractmethod
    def headers(self) -> List[str]:
        pass