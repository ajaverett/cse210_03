from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        
    def get_score(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        if super().get_text() is "*":
            self._message = True
        else:
            self._message = False

        if self._message == True:
            score_change = 100
        else:
            score_change = -100
        return score_change