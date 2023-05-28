import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_airport_info_valid():
    response = client.get("/airport/ABCD")
    assert response.status_code == 200
    assert response.json() == {"icao_code": "ABCD", "name": "Airport ABCD"}

def test_get_airport_info_invalid_length():
    response = client.get("/airport/ABCDE")
    assert response.status_code == 400
    assert response.json() == {"detail": "O código ICAO deve ter 4 caracteres."}

def test_get_airport_info_not_found():
    response = client.get("/airport/WXYZ")
    assert response.status_code == 404
    assert response.json() == {"detail": "O código ICAO WXYZ não é válido."}