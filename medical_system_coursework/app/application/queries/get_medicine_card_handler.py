from typing import Optional
from uuid import UUID
from app.application.dto.medicine_card import MedicineCard
from app.domain.ports.outbound.document_repository import DocumentRepository
from app.domain.ports.outbound.cache_store import CacheStore


class GetMedicineCardHandler:
    """
    Query Handler для отримання повної картки ліків
    """

    def __init__(self, document_repo: DocumentRepository, cache_store: CacheStore):
        self.document_repo = document_repo
        self.cache_store = cache_store

    def handle(self, medicine_id: UUID) -> Optional[MedicineCard]:

        med = self.document_repo.get_by_id(medicine_id)
        if med:
            return MedicineCard(
                medicine_id=med.medicine_id,
                name=med.name,
                chemical_class=med.chemical_class,
                therapeutic_class=med.therapeutic_class,
                price=med.price,
                substitutes=med.substitutes
            )
        return None