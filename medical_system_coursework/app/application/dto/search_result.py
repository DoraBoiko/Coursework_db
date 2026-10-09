from dataclasses import dataclass
from uuid import UUID

@dataclass
class SearchResult:
    """
    DTO для короткого результату пошуку (відображення у списку)
    """
    medicine_id: UUID
    name: str
    price: float