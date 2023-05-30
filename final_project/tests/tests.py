import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):

    def test_english_to_french_null_input(self):
        # Test null input for english_to_french
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

    def test_french_to_english_null_input(self):
        # Test null input for french_to_english
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

    def test_english_to_french_hello(self):
        # Test translation of 'Hello' to French
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

    def test_french_to_english_bonjour(self):
        # Test translation of 'Bonjour' to English
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

if __name__ == '__main__':
    unittest.main()
