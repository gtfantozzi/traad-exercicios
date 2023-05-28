
import requests
from bs4 import BeautifulSoup
from app.core.entities import Airport, AirportInfo
from app.util.logger import logger


class AirportScraper:
    def get_live_airport_info(self, airport: Airport) -> AirportInfo:
        url = f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={airport.icao_code}"
        try:
            with requests.get(url) as res:
                # quando o codigo ICAO é invalido o site faz um redirect
                # pra mesma pagina, contendo msg de nao encontrado
                # verificar no history da resposta evita todo o trabalho
                # do parser e localizar o texto de nao encontrado!
                if len(res.history) > 0:
                    return None
                elif res.status_code == 200:
                    page = res.text
                    soup = self.parse_html_page(page)
                    airport_info = self.get_all_info(soup)
                    return airport_info
                else:
                    logger.warning(f"Falha ao requisitar página. Status code: {res.status_code}")
        except requests.RequestException as err:
            logger.error(f"Erro na função 'get_airport_info': {str(err)}")
        return None

    def parse_html_page(self, page: str) -> BeautifulSoup:
        soup = BeautifulSoup(page, 'html.parser')
        return soup

    def get_all_info(self, soup: BeautifulSoup) -> AirportInfo:
        page_title = soup.title.text

        section_header_elem = soup.select_one('section.page-header.page-header-light h1')
        airport_name, ciad = section_header_elem.text.split('CIAD:')
        airport_name = airport_name.strip()
        ciad = ciad.replace('\n', '').strip()

        sunrise = soup.find('sunrise').text
        sunset = soup.find('sunset').text

        column_right_elem = soup.select('div.col-lg-4.order-sm-12 p')
        taf = column_right_elem[-1].text
        metar = column_right_elem[-2].text

        flight_letters_elem = soup.select(
            'a[target="_blank"][onclick^="javascript:pageTracker._trackPageview(\'/cartas/aerodromos\')"]'
        )

        flight_letters_list = [
            {'name': elem.text, 'link': elem['href']}
            for elem in flight_letters_elem
        ]

        airport_info = AirportInfo(
            name=airport_name,
            ciad=ciad,
            sunrise=sunrise,
            sunset=sunset,
            metar=metar,
            taf=taf,
            flight_letters=flight_letters_list
        )

        return airport_info