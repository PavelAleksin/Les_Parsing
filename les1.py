import requests
from bs4 import BeautifulSoup
import lxml

def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    h1 =soup.find('div','main-top-left').text
    return h1



def main():
    url = 'https://ru.wikipedia.org/'
    print (get_data(get_html(url)))






if __name__ == '__main__':
    main()

#https://ru.wikipedia.org/

#https://wordpress.org/plugins/

#r.status_code
#dir(s)
#r.ok