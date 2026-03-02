from fastapi import APIRouter
from app.models.client import ClientCreate, ClientRead

router = APIRouter()

fake_clients_db = []

@router.post("/", response_model=ClientRead)
def create_client(client: ClientCreate):
    new_client = {"id": len(fake_clients_db) + 1, **client.dict()}
    fake_clients_db.append(new_client)
    return new_client

@router.get("/", response_model=list[ClientRead])
def list_clients():
    return fake_clients_db