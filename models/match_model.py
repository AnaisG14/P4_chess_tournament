class MatchModel:
    """ Instance of match"""

    def __init__(self, player1, player2):
        # player = list ([last_name, ranking], score)
        self.match = (player1, player2)

    def __str__(self):
        return str(self.match)

    def __repr__(self):
        return str(self.match)