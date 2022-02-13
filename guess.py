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
        self._word = []
        self._underscore_word = []
        self._correct_index = None


    def initialize_word(self):
        """Calls the word class and breaks up its returned word into a list and copys the length into a new list of underscores.
        
        Args:
            self (Guess): an instance of Guess.
        """
        _word_class = Word()
        self._word = "hello"

        for letter in self._word:
            self._underscore_word.append('_')               
    

    def check_word(self, player_input):
        """Asks for a player input and compare it to the word to see if its within. If so it will add it to the underscore list in the same index as the index in the word.
        
        Args:
            self (Guess): an instance of Guess.
        """
        int = len(self._word)
        print(int)
        for i in (0, int):
            if player_input in self._word:
                self._correct_index = self._word.index(player_input)
                self._underscore_word[self._correct_index] = player_input
            else:
                return True
        return False

    
    def display_word(self):
        """displayes the underscore word. 
        
        Args:
            self (Guess): an instance of Guess.
        """
        print(self._underscore_word)
