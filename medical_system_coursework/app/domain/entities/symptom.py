from dataclasses import dataclass
from typing import List
from uuid import UUID

@dataclass
class Symptom:
    """
    Використовується як вузол графа для фільтрації препаратів за побічними ефектами
    """
    symptom_id: UUID
    name: str
    medicine_ids: List[UUID]