# https://catertrax.com/why-catertrax/traxers/
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import uniform

def get_html(url):
    user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0'}
    r = requests.get(url, headers=user_agent)
    if r.ok:
        return r.text
    print(r.status_code)

def write_csv(data):
    with open('catertrax.csv', 'a') as f:
        order = ['author', 'since']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_= 'testimonial-container').find_all('article')
    return ts

def get_page_data(ts):
    for t in ts:
        try:
            since = t.find('p', class_='traxer-since').text.strip()
        except:
            since = ''
        try:
            author = t.find('p', class_='testimonial-author').text.strip()
        except:
            author = ''
        data = {'author': author, 'since': since}
        write_csv(data)

def main():
    page = 1
    while True:
        url = 'https://catertrax.com/why-catertrax/traxers/page/{}/'.format(str(page))
        print(url)
        articles = get_articles(get_html(url))
        if articles:
            get_page_data(articles)
            page += 1
            sleep(uniform(1,3))
        else:
            break

if __name__ == '__main__':
    main()