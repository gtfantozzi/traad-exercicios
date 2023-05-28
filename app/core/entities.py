class Airport:
    def __init__(self, icao_code: str):
        self.icao_code = icao_code


class AirportInfo:
    def __init__(self, name: str, ciad: str, sunrise: str, sunset: str, metar: str, taf: str, flight_letters: list):
        self.name = name
        self.ciad = ciad
        self.sunrise = sunrise
        self.sunset = sunset
        self.metar = metar
        self.taf = taf
        self.flight_letters = flight_letters