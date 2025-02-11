import pytest
from fastapi.testclient import TestClient
from ..main import app
from ..database import get_db, Base, engine
from sqlalchemy.orm import sessionmaker

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_users.db"
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)  # Create tables before test
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)  # Clean up after test

@pytest.fixture
def client():
    return TestClient(app)

def test_create_user(client):
    response = client.post("/users/", json={"name": "John Doe", "email": "john@example.com", "password": "secret"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_login(client):
    response = client.post("/auth/login", data={"username": "john@example.com", "password": "secret"})
    assert response.status_code == 200
    assert "access_token" in response.json()
