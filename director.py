
from jumper import Jumper
from guess import Guess
from word import Word

class Director:

    def __init__(self):
        self._is_playing = True
        self._lives = 7

    def start_game(self):
        while self.is_playing:
            self.start_game()
            self.show_screen()
            self.do_checks()

    #input will lead to gameplay
    def start_game(self):
        is_playing = (input("Play Jumper? [y/n] ").lower() in ['y','yes'])
    
    #will display screen first, print whatever Jumper returns
    def show_screen(self):
        screen = Jumper.display_parachute(self.lives)

        if self.is_playing == True:

            print(screen) 

    #if Guess class returns false, lose life
    def do_checks(self):

        guess = Guess()
        lose_life = guess.check_word()
        if lose_life == True:
            self.lives -= 1
        else:
            pass



        


    
        
      