from typing import List
from uuid import UUID
from app.domain.ports.outbound.search_index import SearchIndex

class SearchIndexAdapter(SearchIndex):
    """
    Адаптер-заглушка для Elasticsearch. Виконує простий пошук по рядку замість інвертованого індексу
    """
    def __init__(self):
        self._index = []
        print("[Elasticsearch Stub] Ініціалізація пошукового рушія...")

    def index_bulk(self, data: List[dict]) -> None:
        for item in data:
            self._index.append(item)

    def search_by_text(self, query: str) -> List[UUID]:
        print(f"[Elasticsearch Stub] Виконання повнотекстового пошуку за запитом: '{query}'")

        query = query.lower()
        return [item["id"] for item in self._index if query in item["text"]]