class TournamentModel:
    """ Model of tournament"""

    def __init__(self, informations_tournament):
        self.informations_tournament = informations_tournament
        for attr_name, attr_value in informations_tournament.items():
            setattr(self, attr_name, attr_value)
        #self.tournament_date = (self.start_date, self.end_date)
        self.rounds_name = []
        nb = 1
        rounds_number = self.rounds_number
        while rounds_number:
            self.rounds_name.append(f"Round {nb}")
            nb += 1
            rounds_number -= 1
        self.rounds = []
        self.players = []

    def __str__(self):
        aff = []
        aff.append(self.informations_tournament)
        aff.append(self.rounds)
        aff.append(self.players)
        return str(f"{aff[0]}, rounds : {aff[1]}, players : {aff[2]}")

    def __repr__(self):
        aff = []
        aff.append(self.informations_tournament)
        aff.append(self.rounds)
        aff.append(self.players)
        return str(f"{aff[0]}, rounds : {aff[1]}, players : {aff[2]}")

    def add_players(self, player):
        self.players.append(player)

    def add_rounds(self, round):
        self.rounds.append(round)




