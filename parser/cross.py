import requests
from bs4 import BeautifulSoup

URL = "https://www.lamoda.ru/c/17/shoes-men/?display_locations=all&labels=50377&sf=245"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}


def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_='x-product-card__card x-product-card__card_catalog')
    cross = []
    for item in items:
        price = item.find('div', class_="x-product-card__link x-product-card__hit-area").find_all('span')

        cross.append({
            'brand': item.find('div', class_='x-product-card-description__microdata-wrap').getText(),
            'link': 'https://www.lamoda.ru' + item.find('a', class_="/p/rtlacq548401/shoes-reebok-krossovki/").get('href'),
            'price': price[0].getText() if len(price) == 1 else price[1].getText()

        })
    return cross


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = get_data(html.text)
        return answer
    else:
        raise Exception('Error in parser')
