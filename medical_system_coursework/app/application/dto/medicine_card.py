from dataclasses import dataclass
from typing import List
from uuid import UUID

@dataclass
class MedicineCard:
    """
    DTO для повної картки препарату (відображення при натисканні)
    """
    medicine_id: UUID
    name: str
    chemical_class: str
    therapeutic_class: str
    price: float
    substitutes: List[str]