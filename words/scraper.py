import feedparser
from pymongo import MongoClient


class Scraper:
    URL = 'http://rss.nytimes.com/services/xml/rss/nyt/World.xml'
    URL_MONGO = 'mongodb://localhost:27017/'
    DATABASE_NAME = 'test-database'

    def __init__(self):
        self.client = MongoClient(self.URL_MONGO)
        self.db = self.client[self.DATABASE_NAME]

    def get_last_article(self):
        d = feedparser.parse(self.URL)
        num_article = 0
        while num_article < len(d['entries']):
            last_article = d['entries'][num_article]
            if 'content' in last_article:
                return {
                    "title": last_article['title'],
                    "body": last_article['content'][0]['value']
                }
            else:
                num_article += 1
        raise Exception("Not articles with body")

    def save_article_in_db(self):
        last_article = self.get_last_article()
        article_id = None
        if not self._element_exists(last_article):
            article_id = self.db.articles.insert_one(last_article).inserted_id
        return article_id

    def _element_exists(self, article):
        articles = self.db.articles
        element = articles.find_one(article)
        return element is not None
