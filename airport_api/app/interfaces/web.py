from fastapi import APIRouter, Depends, HTTPException, Path
from app.core.use_cases import GetAirportInfoUseCase
from app.interfaces.gateways import AirportScraper
from app.interfaces.validators import validate_icao_code

router = APIRouter()

airport_scraper = AirportScraper()
get_airport_info_use_case = GetAirportInfoUseCase(airport_scraper)


@router.get("/airport/{icao_code}")
def get_airport_info(icao_code: str = Depends(validate_icao_code)):
    airport_info = get_airport_info_use_case.execute(icao_code)
    if airport_info is None:
        raise HTTPException(status_code=404, detail=f"O código ICAO {icao_code} não é válido.")
    return airport_info