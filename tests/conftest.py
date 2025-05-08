import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def kafka_producer():
    producer = KafkaProducer(...)
    yield producer
    producer.close()