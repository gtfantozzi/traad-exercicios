import re
from typing import Tuple


def validate_icao_code(icao_code: str) -> Tuple[bool, str]:
    if len(icao_code) == 4 and re.match(r'^[A-Za-z]+$', icao_code):
        return False
    return True