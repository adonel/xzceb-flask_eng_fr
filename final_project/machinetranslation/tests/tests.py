import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(french_to_english(""), "")
    
    def test_translate(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

class TestEnglishToFrench(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(english_to_french(""), "")
    
    def test_translate(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

if __name__=='__main__':
    unittest.main()
