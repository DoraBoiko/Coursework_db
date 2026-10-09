from typing import List
from uuid import UUID
from app.domain.ports.outbound.graph_repository import GraphRepository


class GraphAdapter(GraphRepository):
    """
    Адаптер-заглушка для графової БД Neo4j
    """

    def __init__(self):
        print("[Neo4j Stub] Ініціалізація графового сховища...")

    def find_analogues(self, medicine_id: UUID) -> List[UUID]:
        print(f"[Neo4j Stub] Обхід графа для пошуку аналогів препарату {medicine_id}")
        return []