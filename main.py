from scrapping import get_posts_from_habr
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

if __name__ == '__main__':
    get_posts_from_habr(KEYWORDS)