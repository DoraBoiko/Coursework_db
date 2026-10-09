from dataclasses import dataclass
from typing import List
from uuid import UUID

@dataclass
class Medicine:
    medicine_id: UUID
    name: str
    chemical_class: str
    therapeutic_class: str
    price: float
    substitutes: List[str]