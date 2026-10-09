from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

class SearchIndex(ABC):
    """
     Інтерфейс для пошукового рушія (Elasticsearch)
     """
    @abstractmethod
    def search_by_text(self, query: str) -> List[UUID]:
        pass