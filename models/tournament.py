class Tournament:
    """ Model of tournament"""

    def __init__(self, informations_tournament: dict):
        self.informations_tournament = informations_tournament
        for attr_name, attr_value in informations_tournament.items():
            setattr(self, attr_name, attr_value)
        self.tournament_date = (informations_tournament["start_date"], informations_tournament["end_date"])
        self.rounds_name = []
        nb = 1
        rounds_number = self.rounds_number
        while rounds_number:
            self.rounds_name.append(f"Round {nb}")
            nb += 1
            rounds_number -= 1
        self.rounds = []
        self.players = []
        self.results = []

    def display_results(self):
        for player in self.players:
            self.results.append((player.last_name, player.score))
        self.results.sort(key=lambda x: x[1], reverse=True)
        return self.results

    def __str__(self):
        display_tournament = f"{self.informations_tournament}\n Rounds\n"
        for round in self.rounds:
            display_tournament += f"{round}; "
        display_tournament += "Joueurs\n"
        for player in self.players:
            display_tournament += f"{player}; "
        return display_tournament

    def __repr__(self):
        display_tournament = f"{self.informations_tournament}\n Rounds\n"
        for round in self.rounds:
            display_tournament += f"{round}; "
        display_tournament += "Joueurs\n"
        for player in self.players:
            display_tournament += f"{player}; "
        return display_tournament

    def add_players(self, player):
        self.players.append(player)

    def add_rounds(self, round):
        self.rounds.append(round)




