from pprint import pprint

from Keywords import Keyword, Search_articles

if __name__ == '__main__':
    KW = Keyword()
    SR = Search_articles('https://habr.com/ru/all/', 5)
    keyword = KW.KEYWORDS
    block = SR.get_articles_blocks()
    article_list = SR.get_data(block, keyword)

    print()

    for i in range(len(article_list)):

        print('_' * 15, 'NEW_ARTICLE', '_' * 15)
        print(f'Время размещения: {article_list[i]["Время размещения:"]}')
        print(f'Заголовок статьи: {article_list[i]["Заголовок статьи:"]}')
        print(f'Ссылка на статью: {article_list[i]["Ссылка на статью:"]}')
        print(f'Совпавшее слово: {article_list[i]["Совпавшее слово:"]}')
    print()
    print(f'Всего статей соответствующих запросу: {len(article_list)}')
