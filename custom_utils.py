import requests
from bs4 import BeautifulSoup
import re


def categories_(cat):
    result = ''
    for i in cat:
        result += f'#{i} '
    return result


def parsing(url):
    page = requests.get(
        url
    )
    page.encoding = 'utf-8'
    base_url = url[:url.find('.su')+4]
    soup = BeautifulSoup(page.text, 'html.parser')

    img = soup.find(
        'div', {
            'class': 'fimg img-wide'
        }
    ).find(
        'img'
    ).get('src')

    title = soup.find('h1', {
        'class': 'short-title'
    })

    hd = soup.find('div', {
        'class': 'short-label'
    }).text

    category = soup.find('ul', {'class': 'short-list'}).find_all('li')[2].find_all('a')
    categories = []
    for i in category:
        categories.append(i.text)
    try:
        imdb_count = soup.find(
            'div', {
                'class': 'short-rate-in short-rate-imdb'
            }
        ).text
        imdb_count = '.'.join(re.findall(r'[\d]+', imdb_count))
    except:
        imdb_count = None

    description = soup.find(
        'div', {
            'class': 'ftext full-text cleasrfix'
        }
    )

    url_ = base_url + img if img.startswith('/uploads/') else img
    data = [title, hd, categories, imdb_count, description]
    if data[3]:
        text = f'''**🎬 [{data[0]} {data[1]}]({url_})**
**🍿Жанр:** {categories_(data[2])}
**⭐️Рейтинг IMDB:** {data[3]}

🔊{data[4]}

[🎬 Смотреть онлайн]({url})
[👉 Все фильмы](http://hd.kinolive.su/filmy) | [👉 Все сериалы](http://hd.kinolive.su/serialy)'''
    else:
        text = f'''**🎬 [{data[0]} {data[1]}]({url_})**
**🍿Жанр:** {categories_(data[2])}

🔊{data[4]}

[🎬 Смотреть онлайн]({url})
[👉 Все фильмы](http://hd.kinolive.su/filmy) | [👉 Все сериалы](http://hd.kinolive.su/serialy)'''
    return text, url