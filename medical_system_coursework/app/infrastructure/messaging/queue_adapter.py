class QueueAdapter:
    """
    Адаптер-заглушка для черги повідомлень. Поки що імітує чергу в оперативній пам'яті
    """
    def __init__(self):
        self._queue = []
        print("[Queue Stub] Ініціалізація брокера повідомлень...")

    def publish(self, topic: str, message: list) -> None:
        """
        Публікація пакету повідомлень у чергу
        """
        self._queue.append({"topic": topic, "payload": message})
        print(f"[Queue Stub] Опубліковано пакет з {len(message)} об'єктів у топік '{topic}'")

    def consume(self, topic: str) -> list:
        """
        Імітація читання з черги
        """
        messages = [m["payload"] for m in self._queue if m["topic"] == topic]

        self._queue = [m for m in self._queue if m["topic"] != topic]
        print(f"[Queue Stub] Прочитано {len(messages)} пакетів з топіка '{topic}'")
        return messages