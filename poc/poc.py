import json
import logging
from typing import Optional

import requests
from bs4 import BeautifulSoup


# Logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class Scrapper:
    def request(self, icao_code: str) -> Optional[str]:
        """
        Realiza uma requisicao HTTP GET para obter a pagina do aeroporto.

        Args:
            icao_code: O codigo ICAO do aeroporto.

        Returns:
            A pagina como uma string, ou None se a requisicao falhar.
        """
        url = f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={icao_code}"
        try:
            with requests.get(url) as res:
                if res.status_code == 200:
                    return res.text
                else:
                    logger.warning(f"Falha ao requisitar pagina. Status code: {res.status_code}")
        except requests.RequestException as err:
            logger.error(f"Erro na funcao 'request': {str(err)}")
        return None

    def parse_html_page(self, page: str) -> BeautifulSoup:
        """
        Faz o parsing da página HTML e retorna um objeto BeautifulSoup.

        Args:
            page: O conteúdo da página HTML como uma string.

        Returns:
            Um objeto BeautifulSoup que representa a página HTML parseada.
        """
        soup = BeautifulSoup(page, 'html.parser')
        return soup

    def get_all_info(self, soup: BeautifulSoup) -> dict:
        """
        Extrai informações relevantes do aeroporto.

        Args:
            soup: O objeto BeautifulSoup que representa a pagina HTML parseada.

        Returns:
            Um dicionario contendo as informacoes do aeroporto.
        """
        page_title = soup.title.text

        # airport info
        section_header_elem = soup.select_one('section.page-header.page-header-light h1')
        airport_name, ciad = section_header_elem.text.split('CIAD:')

        # normaliza name/ciad strings
        airport_name = airport_name.strip()
        ciad = ciad.replace('\n', '').strip()

        # nascer/por do sol
        sunrise = soup.find('sunrise').text
        sunset = soup.find('sunset').text

        column_right_elem = soup.select('div.col-lg-4.order-sm-12 p')
        taf = column_right_elem[-1].text
        metar = column_right_elem[-2].text

        # cartas disponiveis
        flight_letters_elem = soup.select(
            'a[target="_blank"][onclick^="javascript:pageTracker._trackPageview(\'/cartas/aerodromos\')"]'
        )

        flight_letters_list = [
            {'name': elem.text, 'link': elem['href']}
            for elem in flight_letters_elem
        ]

        airport_info = {
            'page_title': page_title,
            'name': airport_name,
            'ciad': ciad,
            'sunrise': sunrise,
            'sunset': sunset,
            'metar': metar,
            'taf': taf,
            'flight_letters': flight_letters_list
        }

        return airport_info


def print_info(info: dict):
    """
    Printa as informacoes do aeroporto.

    Args:
        info: O dicionario contendo as informacoes do aeroporto.
    """
    print(f"####### {info['page_title']} #######\n")
    print(f"[*] Horário Nascer do Sol: {info['sunrise']}")
    print(f"[*] Horário Por do Sol:    {info['sunset']}")
    print(f"[*] METAR:                 {info['metar']}")
    print(f"[*] TAF:                   {info['taf']}")
    print(f"[*] Cartas disponíveis:")
    for i in info["flight_letters"]:
        print(f"    {i['name']} - {i['link']}")


def main():
    scrapper = Scrapper()
    page = scrapper.request('SBMT')
    if page:
        soup = scrapper.parse_html_page(page)
        airport_info = scrapper.get_all_info(soup=soup)
        print_info(airport_info)

        #printar como json
        #print(json.dumps(airport_info, indent=4))


if __name__ == "__main__":
    main()
