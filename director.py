#BIG WIP

from jumper import Jumper
from guess import Guess
from word import Word

#methods: compare_number; check score; 
class Director:
    #initializes the director class: will run the game
    def __init__(self):
        self.is_playing = True
        self.lives = 6

    #starts the game: will do three methods while playing
    def start_game(self):
        while self.is_playing:
            self.start_game()
            self.show_screen()
            self.get_input()
            self.do_outputs()

    #checks if user wants to play, if yes, then is_playing will be True
    def start_game(self):
        is_playing = (input("Play Jumper? [y/n] ").lower() in ['y','yes'])
    
    #if not playing, loop ends
    def show_screen(self):
        if self.is_playing == True:

            # READ BELOW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            display = Jumper() # <-- idk how this works
            
             #HAVE WORD class RETURN A LIST OF A WORD eg. ['d','o','g']
            #jumper will recieve two inputs, word(from words class) and lives(from director class) to make a screen to be displayed. (it needs to word for the _ _ _ thing, and the lives for the size of the parachute)
            print(display)  

    def get_input(self):
        player_guess = input('guess a letter').lower
        
    def do_outputs(self):
        #guess receives the player_guess and checks it to see if it matches, returns true or false.
        #guess will send this info to jumper to update the screen

        cat = Guess() # <- idk how this works

        if cat == True:
            self.lives -= 1
        else:
            pass





        


    
        
      