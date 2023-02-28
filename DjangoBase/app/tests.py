from django.test import TestCase
from app.utils.wordfinder import WordFinder

class WordFinderTestCase(TestCase):
    def setUp(self):
        self.finder = WordFinder()

    def test_longest_word(self):
        self.assertEqual(self.finder.longest_word('optonoceari'), 'cooperation')
