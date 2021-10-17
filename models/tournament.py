from tinydb import TinyDB

class Tournament:
    """ Model of tournament"""

    def __init__(self, tournament_name, tournament_place, rounds_number, time_controller,
                 manager_description, start_date, end_date):
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.rounds_number = rounds_number
        self.time_controller = time_controller
        self.manager_description = manager_description
        self.start_date = start_date
        self.serialized_start_date = f"{self.start_date}"
        self.end_date = end_date
        self.serialized_end_date = f"{self.end_date}"
        self.date = (start_date, end_date)
        self.rounds_name = [f"Round {nb+1}" for nb in range(int(rounds_number))]
        self.rounds = []
        self.serialized_rounds = []
        self.players = []
        self.serialized_players = []
        self.results = []
        self.serialized_tournament = []

    def create_rounds_name(self):
        nb = 1
        rounds_number = self.rounds_number
        while rounds_number:
            self.rounds_name.append(f"Round {nb}")
            nb += 1
            rounds_number -= 1

    def display_results(self):
        for player in self.players:
            self.results.append((player.last_name, player.first_name, player.score))
        self.results.sort(key=lambda x: x[2], reverse=True)
        return self.results

    def __str__(self):
        display_tournament = f"Nom du tournoi :{self.tournament_name}\n Rounds\n"
        for round in self.rounds_name:
            display_tournament += f"{round}; "
        display_tournament += "Joueurs\n"
        for player in self.players:
            display_tournament += f"{player}; "
        return display_tournament

    def __repr__(self):
        display_tournament = f"Nom du tournoi :{self.tournament_name}\n Rounds\n"
        for round in self.rounds_name:
            display_tournament += f"{round}; "
        display_tournament += "Joueurs\n"
        for player in self.players:
            display_tournament += f"{player}; "
        return display_tournament

    def add_players(self, player):
        self.players.append(player)

    def add_rounds(self, round):
        self.rounds.append(round)

    def serialized(self):
        for round in self.rounds:
            serialized_round = round.serialized()
            self.serialized_rounds.append(serialized_round)
        for player in self.players:
            serialized_player = player.serialized()
            self.serialized_players.append(serialized_player)
        self.serialized_tournament = {
            'tournament_name': self.tournament_name,
            'tournament_place': self.tournament_place,
            'rounds_number': self.rounds_number,
            'time_controller': self.time_controller,
            'manager_description': self.manager_description,
            'start_date': self.serialized_start_date,
            'end_date': self.serialized_end_date,
            'rounds_name': self.rounds_name,
            'rounds': self.serialized_rounds,
            'players': self.serialized_players,
            'result': self.results
        }
        return self.serialized_tournament

    def save_tournament(self):
        self.serialized()
        db = TinyDB('db.json')
        tournament_table = db.table('tournaments')
        tournament_table.truncate()
        tournament_table.insert(self.serialized_tournament)






