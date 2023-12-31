import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open ('cmc.csv','a') as f:
        writer = csv.writer(f)
        pass


def get_page_data(html):
    soup = BeautifulSoup(html,'lxml')
    trs = soup.find('table',class_='sc-beb003d5-3 ieTeVa cmc-table').find('tbody').find_all('tr')
    print (trs)
    for tr in trs:
        tds = tr.find_all('td')
        name = tds[2].find('a').text.partition('/D')[0]
        print (name)

def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))

if __name__  == '__main__':
    main()
