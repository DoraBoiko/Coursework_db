from abc import ABC, abstractmethod

class ConfigureRateUseCase(ABC):
    """Сценарій керування швидкістю генератора навантаження
    """
    @abstractmethod
    def set_rate(self, requests_per_second: int) -> None:
        pass