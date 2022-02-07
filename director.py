
from jumper import Jumper
from guess import Guess
from word import Word

class Director:

    def __init__(self):
        self.is_playing = True
        self.lives = 7

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
        if self.is_playing == True:

            display = Jumper() # <-- idk how this works
            
            print(display) 

    #if Guess class returns false, lose life
    def do_checks(self):

        guess = Guess()
        lose_life = guess.check_word()
        if lose_life == True:
            self.lives -= 1
        else:
            pass



        


    
        
      