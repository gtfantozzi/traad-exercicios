from app.core.entities import Airport, AirportInfo
from app.core.repositories import AirportRepository


class GetAirportInfoUseCase:
    def __init__(self, airport_repository: AirportRepository):
        self.airport_repository = airport_repository

    def execute(self, icao_code: str) -> AirportInfo:
        airport = Airport(icao_code)
        airport_info = self.airport_repository.get_airport_info(airport)
        return airport_info