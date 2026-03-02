import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app import models
from fastapi.testclient import TestClient
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_data():
    db = TestingSessionLocal()
    client1 = models.Client(name="Fernando", email="fernando@test.com")
    db.add(client1)
    db.commit()
    db.refresh(client1)

    invoice1 = models.Invoice(client_id=client1.id, amount=1000, status="pending")
    invoice2 = models.Invoice(client_id=client1.id, amount=500, status="paid")
    db.add_all([invoice1, invoice2])
    db.commit()

    payment1 = models.Payment(invoice_id=invoice2.id, amount=500)
    db.add(payment1)
    db.commit()
    db.close()