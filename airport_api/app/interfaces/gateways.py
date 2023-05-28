from app.core.entities import Airport, AirportInfo
from app.services.scrapper import AirportScraper


# Retornar uma instância de AirportInfo com as informações do aeroporto obtidas
class AirportService:
    def get_live_airport_info(self, airport: Airport) -> AirportInfo:
        scraper = AirportScraper()
        airport_info = scraper.get_live_airport_info(airport)
        return airport_info