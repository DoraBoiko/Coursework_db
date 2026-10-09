from dataclasses import dataclass
from typing import List
from uuid import UUID

@dataclass
class Disease:
    """
    Використовується для встановлення зв’язку між захворюваннями та лікарськими препаратами
    """
    disease_id: UUID
    name: str
    medicine_ids: List[UUID]