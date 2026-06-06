import os

ARTICLES_FOLDER = 'articles'

def get_articles():
    articles = []

    for filename in os.listdir(ARTICLES_FOLDER):
        if filename.endswith('.md'):
            articles.append(filename)
    return articles