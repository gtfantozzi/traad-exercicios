import requests
import json
from typing import Optional
from bs4 import BeautifulSoup


class Scrapper():
    def __init__(self, icao_code=None) -> None:
        self.icao_code = icao_code

    def request(self) -> Optional[str]:
        res = requests.get(
            url=f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={self.icao_code}")
        if res.status_code == 200:
            return res.text
        return None

    def parse_html_page(self, page) -> BeautifulSoup:
        soup = BeautifulSoup(page, 'html.parser')
        return soup

    def get_all_info(self, soup: BeautifulSoup) -> dict:
        page_title = soup.title.text
        # airport info
        section_header_elem = soup.find(
            'section', attrs={'class': 'page-header page-header-light'}).find('h1')
        airport_name, ciad = section_header_elem.text.split('CIAD:')

        # normalize name/ciad strings
        airport_name = airport_name.replace('\xa0', '').strip()
        ciad = ciad.replace('\n', '')

        # nascer/por do sol
        sunrise = soup.find('sunrise').text
        sunset = soup.find('sunset').text

        column_right_elem = soup.find(
            'div', attrs={'class': 'col-lg-4 order-sm-12'}).find_all('p')
        taf = column_right_elem[-1].text
        metar = column_right_elem[-2].text

        # cartas disponiveis
        flight_letters_elem = soup.find_all(
            'a', attrs={"target": "_blank",
                        "onclick": "javascript:pageTracker._trackPageview('/cartas/aerodromos');"})

        flight_letters_list = []
        for i in range(len(flight_letters_elem)):
            flight_letters_list.append(
                {
                    'name': flight_letters_elem[i].text,
                    'link': flight_letters_elem[i]['href']}
            )

        airport_info = {
            'page_title': page_title,
            'icao_code': self.icao_code,
            'name': airport_name,
            'ciad': ciad,
            'sunrise': sunrise,
            'sunset': sunset,
            'metar': metar,
            'taf': taf,
            'flight_letters': flight_letters_list
        }

        return airport_info


def print_info(info):
    print(f"####### {info['page_title']} #######\n")
    print(f"[*] Horário Nascer do Sol: {info['sunrise']}")
    print(f"[*] Horário Por do Sol:    {info['sunset']}")
    print(f"[*] METAR:                 {info['metar']}")
    print(f"[*] TAF:                   {info['taf']}")
    print(f"[*] Cartas disponíveis:")
    for i in info["flight_letters"]:
        print(f"""    {i['name']} - {i['link']}""")


def main():
    scrapper = Scrapper(icao_code='SBBR')
    page = scrapper.request()
    if page:
        soup = scrapper.parse_html_page(page)
        airport_info = scrapper.get_all_info(soup=soup)
        #pretty = json.dumps(airport_info, indent=4)
        #print(pretty)
        print_info(airport_info)


main()
