from app.domain.ports.outbound.cache_store import CacheStore


class ConfigureRateHandler:
    """
    Command Handler для керування швидкістю генератора
    """

    def __init__(self, cache_store: CacheStore):
        self.cache_store = cache_store

    def handle(self, requests_per_second: int) -> None:
        self.cache_store.set("target_rps", requests_per_second, ttl_seconds=86400)

        print(f"[Configure Command] Встановлено нову швидкість генерації: {requests_per_second} RPS")