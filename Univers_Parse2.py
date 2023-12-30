# Задача сделать так, чтобы кортеж был на основе деления по абзацам
# УНИВЕРСАЛЬНЫЙ ПАРСЕР ПО WP сайту

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from Get_url_Img_from_WP import take_url_img_from_wp
from GPT3_other_tags import Chat_converstaion_p, Chat_converstaion_ul_ol, Chat_converstaion_table, Chat_converstaion_quote, Chat_converstaion_ppp
import concurrent.futures

from bs4 import Comment


def get_h2_text_image( url: str):
    string = ''
    print('работаем с урлом - ', url)
    # Исправленный текст для очистки от лишних тегов   **************************************************************
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
               'Accept': '*/*'}
    r = requests.get(url, headers=headers).text
    soup = BeautifulSoup(r, 'html.parser')
    soup0 = BeautifulSoup(r, 'html.parser')



    article = soup.find('div', class_='entry-content')
    for tag in article:
        pass
        # print('--',tag)
    # print(article)


    # КОРРЕКТИРОВКА СТАТЬИ

    # Пройтсь по тегам li и оставить содержимое удалив другие теги
    try:
        lis = article.find_all('li')
        for li in lis:
            inner_tags = li.find_all(True, recursive=False)
            for inner_tag in inner_tags:
                inner_tag.unwrap()
    except:
        print('тегов списка li не нашел')


    # Пройтсь по тегам blockqoute и оставить содержимое удалив другие теги
    try:
        blocks = article.find_all('blockquote')
        for block in blocks:
            inner_tags = block.find_all(True, recursive=False)
            for inner_tag in inner_tags:
                inner_tag.unwrap()
    except:
        print('тегов цитаты не нашел blockqoute')


    # Пройтсь по тегам h2, h3 и оставить содержимое удалив другие теги
    try:
        h2s = article.find_all(['h2', 'h3'])
        for h2 in h2s:
            inner_tags = h2.find_all(True, recursive=False)
            for inner_tag in inner_tags:
                inner_tag.unwrap()
    except:
        print('тегов подзаголовков н2 н3 не нашел')

    #
    # # # УДАЛЕНИЕ СОДЕРЖАНИЯ
    # # try:
    # #     toc_del = article.find('div', id='toc_container')
    # #     toc_del.decompose()
    # # except:
    # #     print('нету содержания для удаления')
    #
    #
    # # # УДАЛЕНИЕ HEADER
    # # try:
    # #     toc_del = article.find('header')
    # #     toc_del.decompose()
    # # except:
    # #     print('нету тега неадер')
    #
    #
    # # Найти внешний тег (например, <div>)
    # try:
    #     divs = soup.find_all('div')
    #     # Распаковать внешний тег, оставив его внутренние теги на том же уровне
    #     for div in divs:
    #         div.unwrap()
    # except:
    #     print('поиск внешнего тега див и его удаление')
    #
    #
    # Найти и удалить все комментарии
    try:
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()
    except:
        print('удаление комментариев в html')
    #
    # Найти все теги <p> содержащие тег <img>. Создаются пустые Р
    try:
        for p_tag in article.find_all('p'):
            img_tag = p_tag.find('img')  # Найти тег <img> внутри тега <p>
            if img_tag:
                # Вырезать тег <img> из тега <p>
                img_tag.extract()
                img_tag.attrs['class'] = 'picture'
                # Вставить тег <img> после тега <p>
                p_tag.insert_after(img_tag)
    except:
        print('-')
    #
    # УДАЛЕНИЕ ПУСТЫХ ТЕГОВ P
    try:
        pp = article.find_all('p')
        for p in pp:
            # print('==', p.get_text())
            if p.get_text() == '':
                p.decompose()
    except:
        print('пустые теги р не найдены')
    #
    # Найти все теги <figure> содержащие тег <img>.
    try:
        for figure_tag in article.find_all('figure'):
            img_tag =figure_tag.find('img')  # Найти тег <img> внутри тега <p>
            if img_tag:
                # Вырезать тег <img> из тега <figure>
                img_tag.extract()
                img_tag.attrs['class'] = 'picture'
                # Вставить тег <img> после тега <p>
                figure_tag.insert_after(img_tag)
    except:
        print('не найдены теги figure')
    #
    # УДАЛЕНИЕ ПУСТЫХ ТЕГОВ FIGURE
    try:
        figures = article.find_all('figure')
        for figure in figures:
            # print('==', p.get_text())
            # if p.get_text() == '':
                figure.decompose()
    except:
        print('нету пстых тегов figure')
    #
    #
    # УДАЛЕНИЕ ТЕГОВ SPAN СОХРАНЯЯ СОДЕРЖИМОЕ
    try:
        spans = article.find_all('span')
        for span in spans:
            span.unwrap()
    except:
        print('теги span не найдены')
    #
    #
    # # УДАЛЕНИЕ ПУСТЫХ ТЕГОВ
    # try:
    #     tags = article.find_all(['p'])
    #     for tag in tags:
    #         if tag.attrs:
    #             del tag.attrs
    # except:
    #     print('пустые теги р не найдены')

    article2 = article.decode_contents()
    return article2



# s = get_h2_text_image('https://zakonguru.com/trudovoe/oplata/zarplata/skolko-poluchayut-vospitateli-v-detskom-sadu-i-ot-chego-zavisit-ix-zarplata.html')
# s = get_h2_text_image('https://sadotpad.ru/interesno/vyrashhivanie-mango-doma/?ysclid=lowlvi8xfs399350783')
s = get_h2_text_image('https://foodandhealth.ru/info/regulyarniy-dnevnoy-son-sohranyaet-molodost-mozga/')
# s = get_h2_text_image('https://polzaivrededy.ru/polza-i-vred-layma-poleznye-svoystva-i-posledstviya-dlya-zdorovya/?ysclid=lpw9xbh9fy441807957')
print('__________ИТОГОВЫЙ КОД__________')
print(s)