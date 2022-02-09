#pull the word class from the word file
from word import Word

#create the guess class
class Guess:
    """Evaluates the players guess
    
    The responsibility of Guess is to take the word and compare it with the players input(guess)

    Attributes:
        initailize_word: initializes the word class to choose a word and then creates the underscore word based on the length of the word.
        check_word: takes the player input and compares it to the letters in its word.
        display_word: displayes the underscore_word in the command terminal.
    """
    def __init__(self):
        """Constructs a new Guess.
        
        Args:
            self (Guess): an instance of Guess.
        """
        player_input = None
        word = []
        underscore_word = []
        correct_index = None


    def initialize_word(self):
        """Calls the word class and breaks up its returned word into a list and copys the length into a new list of underscores.
        
        Args:
            self (Guess): an instance of Guess.
        """
        word_class = Word()
        self.word = word_class.break_word()

        for letter in self.word:
            self.underscore_word.append('_')               
    

    def check_word(self):
        """Asks for a player input and compare it to the word to see if its within. If so it will add it to the underscore list in the same index as the index in the word.
        
        Args:
            self (Guess): an instance of Guess.
        """
        player_input = input("What letter are you guessing?: ").lower()
        if player_input in self.word:
            self.correct_index = self.word.index(player_input)
            self.underscore_word[self.correct_index] = player_input
            return False
        else:
            return True

    
    def display_word(self):
        """displayes the underscore word. 
        
        Args:
            self (Guess): an instance of Guess.
        """
        print(self.underscore_word)
