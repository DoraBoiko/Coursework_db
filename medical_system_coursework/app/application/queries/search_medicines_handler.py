from typing import List
from app.application.dto.search_query import SearchQuery
from app.application.dto.search_result import SearchResult
from app.domain.ports.outbound.search_index import SearchIndex
from app.domain.ports.outbound.document_repository import DocumentRepository
from app.domain.services.query_normalizer import QueryNormalizer


class SearchMedicinesHandler:
    """
    Query Handler для обробки пошукових запитів
    """

    def __init__(self, search_index: SearchIndex, document_repo: DocumentRepository):
        self.search_index = search_index
        self.document_repo = document_repo
        self.normalizer = QueryNormalizer()

    def handle(self, query: SearchQuery) -> List[SearchResult]:

        normalized_text = self.normalizer.normalize(query.raw_query)
        medicine_ids = self.search_index.search_by_text(normalized_text)

        results = []

        for mid in medicine_ids:
            med = self.document_repo.get_by_id(mid)
            if med:
                results.append(SearchResult(medicine_id=med.medicine_id, name=med.name, price=med.price))
        return results