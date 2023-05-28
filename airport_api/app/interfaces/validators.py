from typing import Tuple


def validate_icao_code(icao_code: str) -> Tuple[bool, str]:
    if len(icao_code) != 4:
        return False
    return True