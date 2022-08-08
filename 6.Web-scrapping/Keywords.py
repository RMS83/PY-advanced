from pprint import pprint

import requests
import bs4
import time
from tqdm import tqdm
import re


class Keyword:
    '''
    Класс списка слов для парсинга статей с ХАБРа в превью которых есть данные слова.
    '''

    def __init__(self):
        self.KEYWORDS = ['года', 'дизайн', 'фото', 'web', 'python']


class Search_articles:
    '''
    Класс для извлечения наименования статьи, даты ее размещения и ссылки на статью.
    Парсит данные только по наличию в превью слов из класса Keyword.
    Передаваемые параметры:
    Первый аргумент - основная ссылка на ХАБР https://habr.com/ru/all/
    Второй аргумент - количество страниц для обхода (по дефолту 1-я страница с 20 статьями)
    '''

    def __init__(self, link_, pages=1):
        self.pages = pages
        self.link_ = link_
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ym_uid=1659899304726333049; _ym_d=1659899304; _ym_isad=2',
            'Host': 'habr.com',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

    def _get_resp(self):
        resp = ''
        print(
            f'Подготовка запросов для {self.pages} страниц' if self.pages > 1 else f'Подготовка запроса для 1 страницы')
        for page_num in range(1, self.pages + 1):
            resp_ = requests.get(self.link_ + f'page{page_num}/', headers=self.headers)
            resp_.raise_for_status()
            print(f'Статус запроса стр.{page_num} --> {resp_.status_code}')
            resp += resp_.text

        return resp

    def get_articles_blocks(self):
        '''
        Варим Soup :) из полученной str после запроса get к ХАБРу
        '''
        soup = bs4.BeautifulSoup(self._get_resp(), features='html.parser')
        articles_blocks = soup.find_all('div', class_='tm-article-snippet')
        return articles_blocks

    def _substitutions_in_re(self, regex):
        '''protected метод для работы совместно с .get_data
        regex \t агрумент - регулярное выражение из метода get_data
        \t возвращает значение для замены в nbsp re.sub'''
        return ' ' if regex[1] else ''

    def get_data(self, block, keyword):
        '''Метод get_data для получения информации о статьях на ХАБР
        block \t аргумент - массив текста (class 'bs4.element.ResultSet)
        \t возвращает дату статьи, заголовок статьи и ссылку на статью'''

        print()
        print('Поиск соответствия параметров по статьям')
        a = []
        for articles in tqdm(block, colour='MAGENTA'):
            dict_articles = {}
            time.sleep(0.02)
            articles_body = articles.find_all('div', class_='tm-article-body tm-article-snippet__lead')
            # Собираем список из частей превью заменяя символы 'nbsp' на ' ' и убирая якоря ссылок на полную статью
            res = [re.sub(r'(\xa0)|(Читать[ ]?)?([Дд]ал[ьеш →]*$)|(Подробнее[ →]*$)', self._substitutions_in_re,
                          art.text).strip() for art in articles_body]
            articles_time = articles.find('time')
            articles_head = articles.find('h2')
            articles_href = articles_head.find(class_="tm-article-snippet__title-link")
            for i in keyword:
                if i in res[0]:
                    dict_articles['Время размещения:'] = articles_time.attrs['title']
                    dict_articles['Заголовок статьи:'] = articles_head.text
                    dict_articles['Ссылка на статью:'] = self.link_ + articles_href.attrs['href']
                    dict_articles['Совпавшее слово:'] = i
            a.append(dict_articles) if dict_articles else None
        return a


if __name__ == '__main__':
    KW = Keyword()
    SR = Search_articles('https://habr.com/ru/all/', 2)
    keyword = KW.KEYWORDS
    block = SR.get_articles_blocks()
    pprint(SR.get_data(block, keyword))
