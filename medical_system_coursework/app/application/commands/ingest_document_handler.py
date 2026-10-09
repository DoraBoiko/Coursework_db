from typing import List
from app.domain.entities.medicine import Medicine
from app.domain.ports.outbound.document_repository import DocumentRepository
from app.domain.ports.outbound.search_index import SearchIndex
from app.domain.ports.outbound.graph_repository import GraphRepository
from app.domain.services.shard_key_service import ShardKeyService


class IngestDocumentHandler:
    """
    Command Handler для пакетного запису даних у поліглотне сховище
    """

    def __init__(self, document_repo: DocumentRepository, search_index: SearchIndex, graph_repo: GraphRepository):
        self.document_repo = document_repo
        self.search_index = search_index
        self.graph_repo = graph_repo
        self.shard_key_service = ShardKeyService()

    def handle(self, documents: List[Medicine]) -> None:
        for doc in documents:
            shard_key = self.shard_key_service.compute_key(doc)

        self.document_repo.save_bulk(documents)

        print(f"[Ingest Command] Успішно ініційовано пакетний запис {len(documents)} документів")