from abc import ABC, abstractmethod
from typing import Optional, Any

class CacheStore(ABC):
    """
    Інтерфейс для шару кешування (Redis)
    """
    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        pass

    @abstractmethod
    def set(self, key: str, value: Any, ttl_seconds: int) -> None:
        pass