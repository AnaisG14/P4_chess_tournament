from models import round, tournament, match
from views import display_matches, tournament_view

class LaunchTournament:
    """ Générer les paires de joueurs"""
    def __init__(self, tournament_instance=""):
        self.tournament_view = tournament_view.TournamentView()
        if tournament_instance:
            self.tournament = tournament_instance
        else:
            self.tournament = tournament.Tournament.get(self.get_tournament_in_progress())
        # self.rounds_name = self.tournament.rounds_name
        self.rounds_view = display_matches.DisplayMatches()

    def __call__(self):
        while len(self.tournament.rounds) < int(self.tournament.rounds_number):
            if not self.tournament.rounds:
                self.wait_response("lancer le premier round.")
                self.generate_first_round()
            players_score = self.tournament.players_scores
            self.generate_rounds(f"Round {self.tournament.rounds_name[len(self.tournament.rounds)]}", players_score)
        self.tournament.results = self.tournament.players_scores
        display_results = self.tournament.display_results()
        self.rounds_view.display_classement(display_results)

    def get_tournament_in_progress(self):
        tournament_data = tournament.Tournament.get_tournament_in_progress()
        choice = self.tournament_view.display_tournament_in_progress(tournament_data)
        return tournament_data[int(choice)]
        # if int(choice) in range(len(tournament_data)):
        #     return tournament_data[choice]
        # else:
        #     print("entrez un choix valide")

    def generate_first_round(self):
        self.tournament.players_scores = [[player, 0] for player in self.tournament.players]
        new_round = round.Round(self.tournament.rounds_name[0])
        self.generate_first_pairs(new_round, self.tournament.players_scores)
        self.rounds_view.display_matches(new_round.matches)
        self.wait_response("entrer les scores")
        new_round.add_end_time()
        self.add_score(new_round)
        self.tournament.add_rounds(new_round)

    def add_score(self, round):
        for match in round.matches:
            verification = False
            while not verification:
                score = self.rounds_view.ask_question(f"Score de {match.match[0][0]}")
                test_score = self.verify_score(score)
                if test_score == True:
                    verification = True
                    match.modify_score(score)
                else:
                    print(test_score)
        self.rounds_view.display_score(round.matches)

    def verify_score(self, score_to_test):
        try:
            float(score_to_test)
        except ValueError:
            return f"vous devez entrer un nombre"
        else:
            return True

    def generate_rounds(self, round_name, round_players):
        new_round = round.Round(round_name)
        new_round.matches = []
        self.wait_response("lancer le round suivant.")
        self.generate_pairs(new_round, round_players)
        self.rounds_view.display_matches(new_round.matches)
        self.wait_response("entrer les scores")
        new_round.add_end_time()
        self.add_score(new_round)
        self.tournament.add_rounds(new_round)

        # self.wait_response("Enregistrer")
        # self.tournament.save_tournament()

    def generate_first_pairs(self, round, players_with_score):
        # classer les joueurs en fonction de leur rang
        list_players_sorted = sorted(players_with_score, key=lambda x: x[0].ranking)
        number_of_pairs = len(players_with_score)/2
        nb = 0
        while nb < number_of_pairs:
            player1 = list_players_sorted[nb]
            player2 = list_players_sorted[int(nb + number_of_pairs)]
            round.add_match(match.Match(player1, player2))
            nb += 1

    def generate_pairs(self, round, players):
        # classer les joueurs en fonction de leur score puis de leur rang
        essais = 0
        list_players_sorted = sorted(players,
                                     key=lambda x: (x[1], x[0].ranking))
        while list_players_sorted:
            player1 = list_players_sorted.pop(0)
            player2 = list_players_sorted[0]
            test_pair = self.verify_pairs(player1, player2)
            if test_pair == "ok":
                player2 = list_players_sorted.pop(0)
                round.add_match(match.Match(player1, player2))
            else:
                try:
                    player2 = list_players_sorted.pop(1)
                except IndexError:
                    list_players_sorted = sorted(players,
                                     key=lambda x: (x[1], x[0].ranking))
                    if essais == 0:
                        list_players_sorted[1], list_players_sorted[2] = list_players_sorted[2], list_players_sorted[1]
                    if essais == 1:
                        list_players_sorted[2], list_players_sorted[3] = list_players_sorted[3], list_players_sorted[2]
                    if essais == 2:
                        list_players_sorted[3], list_players_sorted[4] = list_players_sorted[4], list_players_sorted[3]
                    if essais == 3:
                        list_players_sorted[1], list_players_sorted[3] = list_players_sorted[3], list_players_sorted[1]
                    if essais == 4:
                        list_players_sorted[2], list_players_sorted[4] = list_players_sorted[4], list_players_sorted[2]
                    if essais == 5:
                        return "Impossible d'associer les joueurs"
                    essais += 1
                    round.matches.clear()
                else:
                    round.add_match(match.Match(player1, player2))

    def verify_pairs(self, player1, player2):
        for round in self.tournament.rounds:
            for match in round.matches:
                if player1 in match.match:
                    if player2 in match.match:
                        return "impossible"
        return "ok"


    def wait_response(self, question):
        response = self.rounds_view.ask_question(f"Tapez 'q' pour quitter ou 'entrez' pour {question}")
        if response == "q":
            exit()
        else:
            return




