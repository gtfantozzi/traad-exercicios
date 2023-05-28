import pytest
from app.interfaces.validators import validate_icao_code

def test_validate_icao_code_valid():
    assert validate_icao_code("ABCD") is None

def test_validate_icao_code_invalid_length():
    with pytest.raises(ValueError):
        validate_icao_code("ABCDE")