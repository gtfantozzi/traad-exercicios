from app.core.entities import Airport, AirportInfo
from app.interfaces.gateways import AirportService

# Implementar a lógica de persistência/repositório aqui, se necessário
class AirportRepository:
    def get_live_airport_info(self, airport: Airport) -> AirportInfo:
        airport_scraper = AirportService()
        airport_info = airport_scraper.get_live_airport_info(airport)
        return airport_info

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass