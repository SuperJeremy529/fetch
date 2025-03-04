from mongoengine import Document, StringField, ListField, UUIDField
from uuid import uuid4

class Receipts(Document):
    retailer = StringField(required=True, max_length=200)
    purchaseDate = StringField(required=True, max_length=200)
    purchaseTime = StringField(required=True, max_length=200)
    total = StringField(required=True, max_length=200)
    items = ListField(required=True)
    uuid = UUIDField(default=uuid4, required=True, unique=True)

    