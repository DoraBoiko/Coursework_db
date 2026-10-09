class QueryNormalizer:
    """
    Нормалізація тексту запиту
    """
    @staticmethod
    def normalize(raw_query: str) -> str:
        if not raw_query:
            return ""

        words = raw_query.lower().strip().split()
        words.sort()
        return " ".join(words)