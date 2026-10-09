from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from app.domain.entities.medicine import Medicine

class DocumentRepository(ABC):
    """
    CRUD-репозиторій для основної документної БД (MongoDB)
    """
    @abstractmethod
    def get_by_id(self, medicine_id: UUID) -> Optional[Medicine]:
        pass

    @abstractmethod
    def save_bulk(self, medicines: List[Medicine]) -> None:
        pass