from random_words import RandomWords

"""
To install this module - use 'pip install RandomWords'

"""

class Word:

    def __init__(self):
        r = RandomWords()
        self._random_word = r.random_word()
        self.letter_list = []
        pass

    def pick_word(self):
        return self._random_word

    def make_letter_list(self, random_word):
        self.letter_list = list(random_word)
        return self.letter_list