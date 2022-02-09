
from jumper import Jumper
from guess import Guess
from word import Word

class Director:

    def __init__(self):
        self._is_playing = True
        self._lives = 7

    def _start_game(self):
        while self._is_playing:
            self._start_game()
            self._show_screen()
            self._do_checks()

    #input will lead to gameplay
    def _start_game(self):
        is_playing = (input("Play Jumper? [y/n] ").lower() in ['y','yes'])
    
    #will display screen first, print whatever Jumper returns
    def _show_screen(self):

        if self.is_playing == True:

            Jumper.display_parachute(self._lives) 

    #if Guess class returns false, lose life
    def _do_checks(self):

        guess = Guess()
        lose_life = guess.check_word()
        if lose_life == True:
            self.lives -= 1
        else:
            pass



        


    
        
      