from models import round, tournament, match
from views import display_matches, tournament_view
from controllers import management_tournament, home_menu_controller
from utils import verify_response

class LaunchTournament:
    """ Générer les paires de joueurs"""
    def __init__(self, tournament_instance):
        self.tournament_view = tournament_view.TournamentView()
        self.tournament = tournament_instance
        self.rounds_view = display_matches.DisplayMatches()
        self.manage_tournament = management_tournament.ManagementTournament()
        self.quitter = False

    def __call__(self):
        while not self.quitter:
            if len(self.tournament.rounds) < int(self.tournament.rounds_number):
                if not self.tournament.rounds:
                    self.wait_response("lancer le premier round.")
                    self.generate_first_round()
                else:
                    self.generate_rounds(f"Round {self.tournament.rounds_name[len(self.tournament.rounds)]}")
                    self.wait_response("lancer le round suivant.")
            else:
                self.tournament.results = self.tournament.players_scores
                self.tournament.save()
                display_results = self.tournament.display_results()
                self.rounds_view.display_classement(display_results)
                self.wait_response("une autre touche vous affichera de nouveau les résultats")
        return home_menu_controller.HomeMenuController()

    def generate_first_round(self):
        self.tournament.players_scores = [[player, 0] for player in self.tournament.players]
        new_round = round.Round(self.tournament.rounds_name[0])
        self.generate_first_pairs(new_round, self.tournament.players_scores)
        self.rounds_view.display_matches(new_round.matches)
        self.rounds_view.display_information("Entrez les scores pour chaque premier joueur du match")
        new_round.add_end_time()
        self.add_score(new_round)
        self.tournament.add_rounds(new_round)

    def add_score(self, round):
        for match in round.matches:
            verification = False
            while not verification:
                score = self.rounds_view.ask_question(f"Score de {match.opponents[0][0]}")
                test_score = verify_response.check_float(score)
                if test_score == True:
                    verification = True
                    match.modify_score(score)
                else:
                    print(test_score)
        self.rounds_view.display_score(round.matches)

    def generate_rounds(self, round_name):
        new_round = round.Round(round_name)
        new_round.matches = []
        self.generate_pairs(new_round, self.tournament.players_scores)
        self.rounds_view.display_matches(new_round.matches)
        self.rounds_view.display_information("Entrez les scores pour chaque premier joueur du match")
        new_round.add_end_time()
        self.add_score(new_round)
        self.tournament.add_rounds(new_round)


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
            if test_pair:
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
                if player1 in match.opponents:
                    if player2 in match.opponents:
                        return "impossible"
        return True


    def wait_response(self, question):
        response = self.rounds_view.ask_question(f"Tapez 'q' pour retourner au menu principal ou n'importe quelle touche pour {question}")
        if response == "q":
            self.tournament.save()
            self.quitter = True
        else:
            self.quitter = False




