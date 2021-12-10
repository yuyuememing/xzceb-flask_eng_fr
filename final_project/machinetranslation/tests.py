import unittest
from translator import english_to_french
from translator import french_to_english

class TestTranslator(unittest.TestCase):
    def null_english_to_french(self):
        self.assertNotEqual(english_to_french('None'),'')
    def null_english_to_french(self):
        self.assertNotEqual(english_to_french('0'),'0')
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Thanks a lot'),'Merci beaucoup')  

class TestTranslator1(unittest.TestCase):
    def null_french_to_english(self):
        self.assertNotEqual(french_to_english('None'),'')
    def null_french_to_english(self):
        self.assertNotEqual(french_to_english('0'),'0')
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Merci beaucoup'),'Thanks a lot')
if __name__=='__main__':
    unittest.main()