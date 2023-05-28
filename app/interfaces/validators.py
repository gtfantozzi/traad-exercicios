def validate_icao_code(icao_code: str):
    if len(icao_code) != 4:
        raise ValueError("O código ICAO deve ter 4 caracteres. Exemplo: SBMT, SBJD")