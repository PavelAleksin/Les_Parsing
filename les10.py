import requests
from bs4 import BeautifulSoup
from random import choice


def get_proxy():
    html = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table', attrs={'class':'table table-striped table-bordered'}).find_all('tr')[1:11]
    trs
    proxies = []

    for tr in trs:
        tds = tr.find_all('td')
        if 'no' in tds[6].text.strip():
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxy = {'schema': 'http', 'address': ip + ':' + port}
            proxies.append(proxy)

    return proxies[2]


def get_html(url):
    # proxies = {'https': 'ipaddress:5000'}
    p = get_proxy() # {'schema': '', 'address': ''}

    proxy = { p['schema']: p['address']  }
    r = requests.get(url, proxies=proxy, timeout=5)
    return r.json()['origin']




def main():
    url = 'http://httpbin.org/ip'
    print(get_html(url))

if __name__ == '__main__':
    main()
