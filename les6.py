from bs4 import BeautifulSoup
import re

# .find() - поиск значения
# .find_all() - поиск всех значений

# .parent - поиск родительского каталога
# .find_parent() - поиск требуемого каталога

# .parents - поиск родителей
# .find_parents() - поиск требуемых родителей

# .find_next_sibling() - найти следующую
# .find_previous_sibling() - найти предыдущую

# def get_salary(s):
#     pattern = r'\d{1,9}'
#     salary = re.findall(pattern,s)#[0]
#     #salary = re.search(pattern,s).group()
#     print(salary)

def get_copywriter(tag):
    whois = tag.find('div',id = 'whois').text.strip()
    if 'Copywriter' in whois:
        return tag
    return None


def main():
    file = open ('index.html').read()
    soup = BeautifulSoup(file,'lxml')
    # row = soup.find_all('div',{'data-set':'salary'})
    # alena = soup.find('div',string='Alena').find_parent(class_='row')
    # print(alena)
    # copywriters = []
    # persons = soup.find_all('div',class_='row')
    # for person in persons:
    #     cw = get_copywriter(person)
    #     if cw:
    #         copywriters.append(cw)
    # print(copywriters)
    #salary = soup.find_all('div',{'data-set':'salary'})
    #for i in salary:
    #    get_salary(i.text)

    pattern1 = r'\d{1,9}'
    salary = soup.find_all('div',string=re.compile('\d{1,9}'))

    for i in salary:
        print(i.text)


    


if __name__ == '__main__':
    main()



