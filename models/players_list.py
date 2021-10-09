class PlayersList:
    """ Save Players"""

    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        return str(self.players)

    def __repr__(self):
        for player in self.players:
            print(player)

