from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

class GraphRepository(ABC):
    """
    Інтерфейс для роботи з графовою БД (Neo4j)
    """
    @abstractmethod
    def find_analogues(self, medicine_id: UUID) -> List[UUID]:
        pass