import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health():
    assert client.get('/health').status_code == 200

def test_stats_has_columns():
    r = client.get('/stats')
    assert r.status_code == 200
    assert 'columns' in r.json()
