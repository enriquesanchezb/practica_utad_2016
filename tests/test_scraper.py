from unittest import TestCase
from words.scraper import Scraper
import mock
import mongomock


class TestScraper(TestCase):
    def setUp(self):
        self.scraper = Scraper()
        self.scraper.client = mongomock.MongoClient()
        self.scraper.db = self.scraper.client[self.scraper.DATABASE_NAME]

    def tearDown(self):
        self.scraper.db.drop_collection('articles')

    @mock.patch('words.scraper.feedparser.parse')
    def test_get_last_article(self, mock_parse):
        expected_dict = dict(
            body=u'Police officers outside the Brussels courthouse where Salah Abdeslam, a suspect in the Paris attacks, appeared on Thursday. The hearing was postponed until April 7.',
            title=u'Salah Abdeslam, Suspect in Paris Attacks, Seeks Extradition to France')

        rss_article = {'entries': [{
            'content': [{'base': u'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
                         'language': None,
                         'type': u'text/plain',
                         'value': u'Police officers outside the Brussels courthouse where Salah Abdeslam, a suspect in the Paris attacks, appeared on Thursday. The hearing was postponed until April 7.'}],
            'title': u'Salah Abdeslam, Suspect in Paris Attacks, Seeks Extradition to France'
        }]}
        mock_parse.return_value = rss_article
        response_article = self.scraper.get_last_article()

        self.assertEqual(response_article, expected_dict)

    @mock.patch('words.scraper.feedparser.parse')
    def test_last_article_without_body(self, mock_parse):
        rss_article = {'entries': [{
            'title': u'Salah Abdeslam, Suspect in Paris Attacks, Seeks Extradition to France'
        }]}
        mock_parse.return_value = rss_article

        self.assertRaises(Exception, response_article=self.scraper.get_last_article)

    @mock.patch('words.scraper.feedparser.parse')
    def test_last_article_one_with_body_another_without_body(self, mock_parse):
        expected_dict = dict(
            body=u'Police officers outside the Brussels courthouse where Salah Abdeslam, a suspect in the Paris attacks, appeared on Thursday. The hearing was postponed until April 7.',
            title=u'Salah Abdeslam, Suspect in Paris Attacks, Seeks Extradition to France')

        rss_article = {'entries': [{
            'title': u'Salah Abdeslam, Suspect in Paris Attacks, Seeks Extradition to France'
        }, {
            'content': [{'base': u'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
                         'language': None,
                         'type': u'text/plain',
                         'value': u'Police officers outside the Brussels courthouse where Salah Abdeslam, a suspect in the Paris attacks, appeared on Thursday. The hearing was postponed until April 7.'}],
            'title': u'Salah Abdeslam, Suspect in Paris Attacks, Seeks Extradition to France'
        }]}
        mock_parse.return_value = rss_article
        response_article = self.scraper.get_last_article()

        self.assertEqual(response_article, expected_dict)

    def test_article_when_is_not_in_db(self):
        article = dict(
            body=u'Police officers outside the Brussels courthouse where Salah Abdeslam, a suspect in the Paris attacks, appeared on Thursday. The hearing was postponed until April 7.',
            title=u'Salah Abdeslam, Suspect in Paris Attacks, Seeks Extradition to France')

        self.scraper.get_last_article = mock.MagicMock(return_value=article)

        self.assertIsNotNone(self.scraper.save_article_in_db())

    def test_article_when_is_in_db(self):
        article = dict(
            body=u'Police officers outside the Brussels courthouse where Salah Abdeslam, a suspect in the Paris attacks, appeared on Thursday. The hearing was postponed until April 7.',
            title=u'Salah Abdeslam, Suspect in Paris Attacks, Seeks Extradition to France')

        self.scraper.get_last_article = mock.MagicMock(return_value=article)
        self.scraper.db.articles.insert(article)

        self.assertIsNone(self.scraper.save_article_in_db())

    def test_element_doesnt_exist_in_db(self):
        article = dict(
            body=u'Police officers outside the Brussels courthouse where Salah Abdeslam, a suspect in the Paris attacks, appeared on Thursday. The hearing was postponed until April 7.',
            title=u'Salah Abdeslam, Suspect in Paris Attacks, Seeks Extradition to France')

        self.assertFalse(self.scraper._element_exists(article))

    def test_element_exists_in_db(self):
        article = dict(
            body=u'Police officers outside the Brussels courthouse where Salah Abdeslam, a suspect in the Paris attacks, appeared on Thursday. The hearing was postponed until April 7.',
            title=u'Salah Abdeslam, Suspect in Paris Attacks, Seeks Extradition to France')
        objects = [article]
        for obj in objects:
            obj['_id'] = self.scraper.db.articles.insert(obj)
        self.assertTrue(self.scraper._element_exists(article))
