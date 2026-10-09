from dataclasses import dataclass

@dataclass
class SearchQuery:
    """
    DTO для вхідного пошукового запиту від клієнта
    """
    raw_query: str