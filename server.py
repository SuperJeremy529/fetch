from fastapi import FastAPI
from infrastructure.database.repository.receipts import ReceiptsRepository
from dto.receipts import RecepientDTO
from configuration.db_connection import create_database_connection
from service.implementation.simple_pointer_strategy import SimplePointerStrategy
app = FastAPI()


@app.on_event("startup")
def initialize_db_connection():
    create_database_connection()


@app.post("/receipts/process")
def create_receipts(recepient: RecepientDTO):
    respository = ReceiptsRepository() 
    id = respository.create(recepient_dto=recepient)
    return {"id": id}



@app.get("/receipts/{id}/points")
def read_item(id: str):
    respository = ReceiptsRepository() 
    recepient_dto = respository.get(recepient_uuid=id)
    strategy = SimplePointerStrategy()
    points = strategy.execute(recepient_dto=recepient_dto)
    return {"points": int(points)}
    

