from typing import Dict, Any
from app.application.dto.search_query import SearchQuery
from app.application.queries.search_medicines_handler import SearchMedicinesHandler


class SearchController:
    """
    REST-контролер для прийому HTTP-запитів від користувача.
    """
    def __init__(self, search_handler: SearchMedicinesHandler):
        self.search_handler = search_handler

    def search_medicines(self, request_args: Dict[str, Any]) -> Dict[str, Any]:
        print("[SearchController] Отримано запит на пошук ліків")

        query_text = request_args.get("q", "")
        query_dto = SearchQuery(raw_query=query_text)

        results = self.search_handler.handle(query_dto)

        return {
            "status": "success",
            "count": len(results),
            "data": [res.__dict__ for res in results]
        }