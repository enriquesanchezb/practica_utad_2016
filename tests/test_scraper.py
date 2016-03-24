from unittest import TestCase
from words.scraper import Scraper
import mock


class TestScraper(TestCase):
    def setUp(self):
        self.scraper = Scraper()

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
        },{
            'content': [{'base': u'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
                         'language': None,
                         'type': u'text/plain',
                         'value': u'Police officers outside the Brussels courthouse where Salah Abdeslam, a suspect in the Paris attacks, appeared on Thursday. The hearing was postponed until April 7.'}],
            'title': u'Salah Abdeslam, Suspect in Paris Attacks, Seeks Extradition to France'
        }]}
        mock_parse.return_value = rss_article
        response_article = self.scraper.get_last_article()

        self.assertEqual(response_article, expected_dict)