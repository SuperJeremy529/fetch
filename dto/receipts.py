from pydantic import BaseModel


class RecepientDTO(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: list[dict]
    total: str

    class Config:
        extra = "forbid"

