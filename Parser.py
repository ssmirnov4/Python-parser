from bs4 import BeautifulSoup
import requests
import urllib3


def parse():
    urllib3.disable_warnings()  # отключаем варнинги чтобы пустило на сайт
    url = 'https://omgtu.ru/general_information/faculties/'
    page = requests.get(url, verify=False)
    print(page.status_code)  # ответ от страницы
    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.findAll('ul')  #находим тег "ul", где нужные нам данные
    description = ''
    for data in block:  # бегаем по блоку
        if data.find('p'):  # находим нужный тег
            description = data.text  # записываем с него текст
    description = description.strip() #убираем при выводе в файл верхние и нижние сносы строк
    description = description.replace('\n\n\n\n', '') #убираем при выводе в файл сносы строк между названиями факультетов
    return description


def file(faculties):
    f = open('faculties.txt', 'w')
    f.write(faculties)
    f.close()