from unittest import TestCase
from words.words import Words

class TestVirgilio(TestCase):
    def test_count_words(self):
        texto = "hola"
        w = Words()
        self.assertEquals(w.count_words(texto), {'hola': 1})

    def test_count_words_uppercase_lowercase(self):
        texto = "hola Hola"
        w = Words()
        self.assertEquals(w.count_words(texto), {'hola': 2})

    def test_count_words_log_text(self):
        texto = "hola que tal como estas? yo bien y tu. hola amigo."
        resultado = {'amigo': 1, 'bien': 1, 'que': 1, 'estas': 1, 'yo': 1, 'tal': 1, 'tu': 1, 'como': 1, 'hola': 2}
        w = Words()
        self.assertEquals(w.count_words(texto), resultado)