class TournamentView:
    """ User interface using tournament model """

    def __init__(self):
        self.questions = []
        self.verification = False
        self.keys = []

    def add_questions(self, question, question_variable, verify_question="", default_value=""):
        """ Add questions to the manager to create the tournament.
         Each question must contain the question, the variable name to save the question
         in a dictionnary, the default_value and the test to verify the question"""
        self.questions.append((question, question_variable, verify_question, default_value))

    def ask_questions(self, question):
        return input(question)

    def display_responses(self, description_tournament):
        print(f"Vous venez de créer le tournoi suivant: \n"
              f"Nom du tournoi: {description_tournament.tournament_name}\n"
              f"Lieu du tournois: {description_tournament.tournament_place}\n"
              f"Dates: {description_tournament.date}")

    def display_tournament_in_progress(self, tournaments_in_progress):
        for key, value in tournaments_in_progress.items():
            print(f"{key}- {value['tournament_name']} à {value['tournament_place']} du "
                  f"{value['start_date']} au {value['end_date']}")
        return input("Entrez le numéro du tournoi que vous souhaitez reprendre :")

    def display_tournament_name(self, tournaments):
        for tournament in tournaments:
            print(f"{tournament.tournament_name}, à {tournament.tournament_place}, {tournament.date}")

    def display_rounds(self, tournament):
        for round in tournament.rounds:
            print(f"nom: {round.round_name}")
            print(f"Début: {round.datetime_start} ; Fin: {round.datetime_end}")

    def display_matches(self, tournament):
        for round in tournament.rounds:
            print(f"nom: {round.round_name}")
            for match in round.matches:
                print(f"{match.opponents}: vainqueur: {match.winner}")






