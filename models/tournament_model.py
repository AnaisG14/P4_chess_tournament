class TournamentModel:
    """ Model of tournament"""

    def __init__(self, informations_tournament):
        self.informations_tournament = informations_tournament
        for attr_name, attr_value in informations_tournament.items():
            setattr(self, attr_name, attr_value)
        self.rounds_list = []
        self.players_index = []

    def __str__(self):
        return str(self.informations_tournament)



