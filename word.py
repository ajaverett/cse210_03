import random

class Word:

    def __init__(self):
        self._random_word = " "
        self.letter_list = []
        pass

    def _pick_word(self):
        # Opens a text file containing basically every single English word, as well as some random ones we
        # added for fun. It then selects one of these words and passes it to the next function.
        with open("lower_words.txt", "r") as file:
            allwords = file.read()
            words = list(map(str, allwords.split()))
            self._random_word = random.choice(words)
        return self._random_word

    def _make_letter_list(self, random_word):
        # This function takes the word being passed to it from pick_word and turns it into an array
        # of letters so it can be used by the game to make the spaces required, as well as providing
        # something we can check if the guessed letter is in.
        self.letter_list = list(random_word)
        return self.letter_list