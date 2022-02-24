import unittest
from translator import *

class TestEnglishToFrechTranslator(unittest.TestCase):
    def test_null_value(self):
        self.assertEqual(english_to_french(None), "Please type or paste a word or phrase in English.")

    
    def test_valid_arguement(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestFrenchTpEnglishTranslation(unittest.TestCase):
    def test_null_value(self):
        self.assertEqual(french_to_english(None), "Please type or paste a word or phrase in French.")
    
    def test_valid_arguement(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()