from dto.receipts import RecepientDTO
from infrastructure.database.models.receipts import Receipts
from infrastructure.database.repository.base_repository import BaseRepository

class ReceiptsRepository(BaseRepository):
    def create(self, recepient_dto: RecepientDTO):
        instance = Receipts(
            retailer=recepient_dto.retailer,
            purchaseDate=recepient_dto.purchaseDate,
            purchaseTime=recepient_dto.purchaseTime,
            items=recepient_dto.items, 
            total=recepient_dto.total
        )
        instance.save()
        return str(instance.uuid)
    
    def get(self, recepient_uuid: str):
        instance = Receipts.objects.get(uuid=recepient_uuid)
        return RecepientDTO(
            retailer=instance.retailer,
            purchaseDate=instance.purchaseDate,
            purchaseTime=instance.purchaseTime,
            items=instance.items, 
            total=instance.total            
        )