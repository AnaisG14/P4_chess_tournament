class Match:
    """ Instance of match"""

    def __init__(self, player1, player2):
        # player = list ([last_name, ranking], score)
        self.player1 = player1
        self.player2 = player2
        self.match = (player1, player2)

    def __str__(self):
        return f"{self.player1} contre {self.player2}"

    def __repr__(self):
        return f"{self.player1} contre {self.player2}"
