
from jumper import Jumper
from guess import Guess
from word import Word

class Director:

    def __init__(self):
        self._guess = Guess()
        self._is_playing = self._guess.check_win()
        self._guess.initialize_word()
        self._lives = 8

    def _start_game(self):
        self._start_input()
        if self._is_playing:
            while self._guess.check_win():
                self._show_screen()
                self._do_checks()

    #input will lead to gameplay
    def _start_input(self):
        self._is_playing = (input("Play Jumper? [y/n] ").lower() in ['y','yes'])
    
    #will display screen first, print whatever Jumper returns
    def _show_screen(self):
        jumper = Jumper()
        if self._is_playing == True:

            jumper.display_parachute(self._lives) 

    #if Guess class returns false, lose life
    def _do_checks(self):
        player_input = input("What letter are you guessing?: ").lower()
        lose_life = self._guess.check_word(player_input)
        self._guess.display_word()
        if lose_life == True:
            self._lives -= 1
        else:
            pass
        if self._lives <= 0:
            self._is_playing = False



        


    
        
      