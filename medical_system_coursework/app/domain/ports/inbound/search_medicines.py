from abc import ABC, abstractmethod

class SearchMedicinesUseCase(ABC):
    """
    Сценарій використання для пошуку ліків
    """
    @abstractmethod
    def execute(self, query_text: str) -> list:
        pass