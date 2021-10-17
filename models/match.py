from models import player

class Match:
    """ Instance of match"""

    def __init__(self, player1, player2):
        # player = list ([last_name, ranking], score)
        self.player1 = player1
        self.player2 = player2
        self.match = (player1, player2)
        self.serialized_match = []

    def __str__(self):
        return f"{self.player1} contre {self.player2}"

    def __repr__(self):
        return f"{self.player1} contre {self.player2}"

    def serialized(self):
        player1 = self.player1.serialized()
        player2 = self.player2.serialized()
        self.serialized_match = {
            'player1': player1,
            'player2': player2,
            'match': (player1, player2)
        }
        return self.serialized_match
