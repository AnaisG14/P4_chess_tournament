class TournamentList:
    """ List of instance of tournament"""

    def __init__(self):
        self.tournaments = []

    def add_tournament(self, tournament):
        self.tournaments.append(tournament)

    def save_tournament(self, tournament):
        pass

    def __str__(self):
        return str(self.tournaments)

    def __repr__(self):
        return str(self.tournaments)