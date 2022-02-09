import random

class Word:

    def __init__(self):
        self._random_word = " "
        self.letter_list = []
        pass



    def pick_word(self):
        with open("lower_words.txt", "r") as file:
            allwords = file.read()
            words = list(map(str, allwords.split()))
            self._random_word = random.choice(words)
        return self._random_word

    def make_letter_list(self, random_word):
        self.letter_list = list(random_word)
        return self.letter_list