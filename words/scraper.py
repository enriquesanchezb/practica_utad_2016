import feedparser


class Scraper:
    URL = 'http://rss.nytimes.com/services/xml/rss/nyt/World.xml'

    def __init__(self):
        pass

    def get_last_article(self):
        d = feedparser.parse(self.URL)
        num_article = 0
        while num_article < len(d['entries']):
            last_article = d['entries'][num_article]
            if 'content' in last_article:
                return {"title": last_article['title'], "body": last_article['content'][0]['value']}
            else:
                num_article += 1
        raise Exception("Not articles with body")