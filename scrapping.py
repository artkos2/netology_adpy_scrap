import requests
from bs4 import BeautifulSoup

HEDERS = {
    'Cookie': '_ga=GA1.2.843930926.1655296268; _ym_uid=1591090729127343407; _ym_d=1655296269; hl=ru; fl=ru; __gads=ID=6d11c28c5d74812f:T=1655311415:S=ALNI_MYNwKvx2rukcu5jEDoGCOSZMnb6jQ; habr_web_home_feed=/all/; _ym_isad=2; _gid=GA1.2.1079387842.1659451577; _gat_gtag_UA_726094_1=1',
    'Host': 'habr.com',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'macOS',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
def get_posts_from_habr(my_keywords):
    res = requests.get('https://habr.com/ru/all/', headers=HEDERS)
    soup = BeautifulSoup(res.text, 'html.parser')
    posts = soup.find_all(class_='tm-article-snippet')
    for post in posts:
        keywords = post.find_all(class_='tm-article-snippet__hubs-item')
        for keyword in keywords:
            if keyword.text.replace('*', '').strip().lower() in my_keywords:
                hub = post.find('a', class_='tm-article-snippet__title-link')
                url = 'https://habr.com' + str(hub.attrs.get('href'))
                date = post.find('time').attrs.get('title')
                print(date + ' - ' + hub.text + ' - ' + url)
