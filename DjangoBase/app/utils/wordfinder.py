import requests

class WordFinder:
    def __init__(self, url = '') -> None:
        """Initialize the WordFinder class.
        Args:
            url (str): The URL to the word list. Defaults to ''."""
        
        self.words: set = set()
        if url == '':
            url = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt'
        response = requests.get(url)
        for line in response.iter_lines():
            self.words.add(line.decode('utf-8'))
                
    def longest_word(self, letters):
        """Find the longest word that can be made from the given letters.
        Args:
            letters (str): The letters to use.
        Returns:
            str: The longest word that can be made from the given letters."""
        
        letters = set(letters)
        max_length = 0
        max_word = ''
        for word in self.words:
            if set(word).issubset(letters) and len(word) > max_length:
                max_length = len(word)
                max_word = word
        return max_word
