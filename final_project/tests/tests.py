import unittest
import machinetranslation.translator as translator


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(translator.english_to_french("Hello"), "Bonjour")
        self.assertEqual(translator.english_to_french("Good morning"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(translator.french_to_english("Ça va"), "How are you")


unittest.main()
