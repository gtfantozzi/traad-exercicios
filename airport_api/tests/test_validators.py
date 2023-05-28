import pytest
from app.interfaces.validators import validate_icao_code

def test_validate_icao_code_valid():
    assert validate_icao_code("SBMT") is True

def test_validate_icao_code_invalid_length():
    assert validate_icao_code("ABCDE") is False