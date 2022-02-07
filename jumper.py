class Jumper:
    def __init__(self):
        self._parachute_list = ['    _______ ' , '   /       \ ', '  / \ / \ / \ ', '  \  | _ |  / ', '  o( ͡° ͜ʖ ͡°)o ', '   \/ |_|\/ ', "     // \\  ", '     U   U ']

    def display_parachute(self, lives):
        if lives == 0:
            return False

        for i in range(0, (8- lives)):
            self._parachute_list.remove(self._parachute_list[0])
            
        for i in range(0,lives):
           print (self._parachute_list[i])       