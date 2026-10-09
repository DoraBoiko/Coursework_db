from abc import ABC, abstractmethod

class IngestDocumentUseCase(ABC):
    """
    Сценарій пакетного завантаження даних
    """
    @abstractmethod
    def execute(self, documents: list) -> None:
        pass