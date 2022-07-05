import unittest
from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french(None),"")
        self.assertNotEqual(english_to_french(""),"Bonjour")

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english(None),"")
        self.assertNotEqual(french_to_english(""),"Hello")

unittest.main()