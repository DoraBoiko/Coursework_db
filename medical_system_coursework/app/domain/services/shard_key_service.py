from app.domain.entities.medicine import Medicine

class ShardKeyService:
    """
    Обчислення ключа розподілу (Shard Key) для MongoDB.
    """
    @staticmethod
    def compute_key( medicine: Medicine) -> dict:
        return {
            "therapeutic_class": medicine.therapeutic_class,
            "medicine_id": str(medicine.medicine_id)
        }