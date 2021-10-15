import bs4
import requests
from bs4 import BeautifulSoup

# определяем список ключевых слов
KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'Big Data'}


# Ваш код
ret = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(ret.text, 'html.parser')
articles = soup.find_all('article')


for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.find('span').text for hub in hubs)
    if KEYWORDS & hubs:
        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        link = 'https://habr.com' + href
        dates = article.find(class_='tm-article-snippet__datetime-published').time['datetime']
        print('<', dates, '>', '-', '<', article.find('h2').text, '>', '-', '<', link, '>')
