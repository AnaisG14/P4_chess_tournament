from tinydb import TinyDB
from models import round, player
from models import connexion_db

class TournamentManager:
    """ serialize and deserialize players and save them into a tinyDB"""
    manage_db = connexion_db.ManagementDB()

    @classmethod
    def deserialize(cls, serialized_tournament):
        tournament_name = serialized_tournament['tournament_name']
        tournament_place = serialized_tournament['tournament_place']
        rounds_number = serialized_tournament['rounds_number']
        time_controller = serialized_tournament['time_controller']
        manager_description = serialized_tournament['manager_description']
        start_date = serialized_tournament['start_date']
        end_date = serialized_tournament['end_date']
        rounds_name = serialized_tournament['rounds_name']
        rounds = []
        deserialized_rounds = serialized_tournament['rounds']
        deserialized_results = serialized_tournament['results']
        for serialized_round in deserialized_rounds:
            rounds.append(round.Round.get(serialized_round))
        players = []
        deserialized_players = serialized_tournament['players']
        for serialized_player in deserialized_players:
            players.append(player.Player.get(serialized_player))
        players_scores = []
        deserialized_player_score = serialized_tournament['players_scores']
        for serialized_player_score in deserialized_player_score:
            players_scores.append([player.Player.get(serialized_player_score[0]), serialized_player_score[1]])
        results = []
        for serialilized_result in deserialized_results:
            result_player = [player.Player.get(
                serialilized_result[0]), serialilized_result[1]]
            results.append(result_player)
        informations_to_create_tournament = {'tournament_name': tournament_name,
                                             'tournament_place': tournament_place,
                                             'rounds_number': rounds_number,
                                             'time_controller': time_controller,
                                             'manager_description': manager_description,
                                             'start_date': start_date,
                                             'end_date': end_date,
                                             'rounds_name': rounds_name,
                                             'rounds': rounds,
                                             'players': players,
                                             'players_scores': players_scores,
                                             'results': results
                                             }
        return informations_to_create_tournament

    @classmethod
    def get_all(cls):
        all_tournaments = []
        results_db = cls.manage_db.get('tournaments')
        for result in results_db:
            deserialized_tournament = cls.deserialize(result)
            all_tournaments.append(Tournament(**deserialized_tournament))
        return all_tournaments

    @classmethod
    def get_one(cls, serialized_tournament):
        deserialized_tournament = cls.deserialize(serialized_tournament)
        return Tournament(**deserialized_tournament)

    @classmethod
    def save_all(cls, tournaments):
        cls.manage_db.clear_tournaments()
        for tournament in tournaments:
            cls.manage_db.save('tournaments', tournament.serialize())

    @classmethod
    def save_one(cls, serialized_tournament):
        cls.manage_db.save('tournaments', serialized_tournament)


class Tournament:
    """ Model of tournament"""
    manager = TournamentManager()

    def __init__(self, tournament_name, tournament_place, rounds_number, time_controller,
                 manager_description, start_date, end_date, rounds_name=[], rounds=[],
                 players=[], players_scores=[], results=[]):
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.rounds_number = rounds_number
        self.time_controller = time_controller
        self.manager_description = manager_description
        self.start_date = start_date
        self.end_date = end_date
        if rounds_name:
            self.rounds_name = rounds_name
        else:
            self.rounds_name = [f"Round {nb+1}" for nb in range(int(rounds_number))]
        if rounds:
            self.rounds = rounds
        else:
            self.rounds = []
        self.players = players
        self.players_scores = players_scores
        self.results = results

        self.serialized_start_date = f"{self.start_date}"
        self.serialized_end_date = f"{self.end_date}"
        self.date = (start_date, end_date)
        self.serialized_rounds = []
        self.serialized_players = []
        self.serialized_players_scores = []
        self.serialized_results = []
        self.save_tournament = connexion_db.ManagementDB()

    def create_rounds_name(self):
        nb = 1
        rounds_number = self.rounds_number
        while rounds_number:
            self.rounds_name.append(f"Round {nb}")
            nb += 1
            rounds_number -= 1

    def display_results(self):
        self.results.sort(key=lambda x: x[1], reverse=True)
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

    def serialize(self):
        for each_round in self.rounds:
            serialized_round = each_round.serialize()
            self.serialized_rounds.append(serialized_round)
        for each_player in self.players:
            serialized_player = each_player.serialize()
            self.serialized_players.append(serialized_player)
        for each_player in self.players_scores:
            serialized_player1 = each_player[0].serialize()
            self.serialized_players_scores.append([serialized_player1, each_player[1]])
        for each_result in self.results:
            serialized_result = each_result[0].serialize()
            self.serialized_results.append([serialized_result, each_result[1]])
        serialized_tournament = {
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
            'players_scores': self.serialized_players_scores,
            'results': self.serialized_results
        }
        return serialized_tournament

    def save(self):
        self.manager.save_one(self.serialize())

    @classmethod
    def get_one(cls, serialized_tournament):
        return cls.manager.get_one(serialized_tournament)

    @classmethod
    def get_all(cls):
        return cls.manager.get_all()








