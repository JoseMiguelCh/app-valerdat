import requests

class WordFinder:
    def __init__(self, source: str | list = '', type = 'external') -> None:
        """Initialize the WordFinder class.
        Args:
            url (str): The URL to the word list. Defaults to ''."""
        
        self.words: set = set()
        response = ''
        if source == '' and type == 'external':
            source = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt'
            response = requests.get(source)
            for line in response.iter_lines():
                self.words.add(line.decode('utf-8'))
        else: 
            for item in source:
                self.words.add(item)
        
                
    def longest_word(self, letters):
        """Find the longest word that can be made from the given letters.
        Args:
            letters (str): The letters to use.
        Returns:
            str: The longest word that can be made from the given letters."""
        def is_subset(word1, word2):
            return all(word1.count(c) <= word2.count(c) for c in set(word1))

        valid_words = [w for w in self.words if is_subset(w, letters)]
        if not valid_words:
            return None
        return max(valid_words, key=len)