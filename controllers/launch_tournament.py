from models import round
from views import display_matches

class LaunchTournament:
    """ Générer les paires de joueurs"""
    def __init__(self, tournament):
        self.tournament = tournament
        self.rounds_name = tournament.rounds_name
        self.rounds_view = display_matches.DisplayMatches()
        self.verification = False

    def __call__(self):
        self.wait_response("lancer le premier round.")
        self.generate_first_round()
        nb = 1
        while nb < len(self.tournament.rounds_name):
            self.generate_rounds(f"Round {nb+1}")
            nb += 1
        results = self.tournament.display_results()
        self.rounds_view.display_classement(results)


    def generate_first_round(self):
        new_round = round.Round(self.tournament, self.tournament.rounds_name[0])
        new_round.generate_first_pairs()
        self.rounds_view.display_matches(new_round.matches)
        self.tournament.add_rounds(new_round)
        self.wait_response("entrer les scores")
        new.round.add_end_time()
        self.add_score(new_round)


    def add_score(self, round):
        for match in round.matches:
            while not self.verification:
                score1 = self.rounds_view.ask_question(f"Score de {match.player1}")
                test_score = self.verify_score(score1)
                if test_score == True:
                    self.verification = True
                else:
                    print(test_score)
            self.verification = False
            while not self.verification:
                score2 = self.rounds_view.ask_question(f"Score de {match.player2}")
                test_score = self.verify_score(score2)
                if test_score == True:
                    self.verification = True
                else:
                    print(test_score)
            self.verification = False
            match.player1.modify_score(match.player1.score + float(score1))
            match.player2.modify_score(match.player2.score + float(score2))
        self.rounds_view.display_score(self.tournament.players)

    def verify_score(self, score_to_test):
        try:
            float(score_to_test)
        except ValueError:
            return f"vous devez entrer un nombre"
        else:
            return True

    def generate_rounds(self, round_name):
        new_round = round.Round(self.tournament, round_name)
        self.wait_response("lancer le round suivant.")
        new_round.generate_pairs()
        self.rounds_view.display_matches(new_round.matches)
        self.tournament.add_rounds(new_round)
        self.wait_response("entrer les scores")
        new.round.add_end_time()
        self.add_score(new_round)

    def wait_response(self, question):
        response = self.rounds_view.ask_question(f"Tapez 'q' pour quitter ou 'entrez' pour {question}")
        if response == "q":
            exit()
        else:
            return




