__author__ = 'enriquesanchez'

import re

import nltk

regex_url = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    # domain...
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
    r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

stopwords = nltk.corpus.stopwords.words('english') + [
    '.',
    '..',
    '...',
    ',',
    '--',
    '\'s',
    '?',
    ')',
    '(',
    ':',
    '\'',
    '\'re',
    '"',
    '-',
    '}',
    '{',
    '<',
    '>',
    '=',
    'these',
    'there',
    'they',
    'those',
    'whose',
    'ours',
    'your',
    'yours',
    'others',
    'anothers'
]

ignorewords = {'the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'for', 'by', 'are', 'i', 'you', 'he', 'she', 'we', 'do',
               'does', 'did', 'say', 'said', 'says', 'tell', 'told', 'what', 'where', 'when', 'how', 'who', 'whose',
               'why', 'would'}


def is_url(word):
    return regex_url.match(word)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class Words:
    def __init__(self):
        pass

    def count_words(self, text):
        w_aux = nltk.wordpunct_tokenize(text)
        scored_words = {}
        for word in w_aux:
            word = word.lower()
            if word not in stopwords and \
                    word not in ignorewords and \
                    len(word) > 1 and \
                    not is_url(word) and \
                    not is_number(word):
                try:
                    scored_words[word] += 1
                except:
                    scored_words[word] = 1
        return scored_words