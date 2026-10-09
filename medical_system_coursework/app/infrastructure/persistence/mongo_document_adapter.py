from typing import List, Optional
from uuid import UUID
from app.domain.entities.medicine import Medicine
from app.domain.ports.outbound.document_repository import DocumentRepository

class MongoDocumentAdapter(DocumentRepository):
    """
    Адаптер-заглушка для MongoDB. Зберігає дані у словнику Python (In-Memory)
    """
    def __init__(self):
        self._collection = {}
        print("[MongoDB Stub] Ініціалізація підключення до кластера (імітація)...")

    def get_by_id(self, medicine_id: UUID) -> Optional[Medicine]:
        print(f"[MongoDB Stub] Читання документа з ID: {medicine_id}")
        return self._collection.get(medicine_id)

    def save_bulk(self, medicines: List[Medicine]) -> None:
        print(f"[MongoDB Stub] Пакетне збереження {len(medicines)} документів...")
        for med in medicines:
            self._collection[med.medicine_id] = med