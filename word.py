import random
class Word:

    def __init__(self):
        self._word_list = ["Gimbus", "Elf", "Your", "Mom", "Cookie", "Jack", "Train"]
        self._random_word = random.choice(self._word_list)
        self.letter_list = []
        pass

    def pick_word(self):
        return self._random_word

    def make_letter_list(self, random_word):
        self.letter_list = list(random_word)
        return self.letter_list