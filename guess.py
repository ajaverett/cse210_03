from word import Word

class Guess:
    def __init__(self):
        player_input = None
        word = []
        underscore_word = []
        correct_index = None


    def initialize_word(self):
        word_class = Word()
        self.word = word_class.break_word()

        for letter in self.word:
            self.underscore_word.append('_')               
    

    def check_word(self):
        player_input = input("What letter are you guessing?: ").lower()
        if player_input in self.word:
            self.correct_index = self.word.index(player_input)
            self.underscore_word[self.correct_index] = player_input
            return False
        else:
            return True

    
    def display_word(self):
        print(self.underscore_word)
