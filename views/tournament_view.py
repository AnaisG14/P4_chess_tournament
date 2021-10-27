class TournamentView:
    """ User interface using tournament model """

    def __init__(self):
        self.questions = []
        self.verification = False
        self.keys = []

    def add_questions(self, question, question_variable, verify_question="", default_value=""):
        """ Add questions to the manager to create the tournament.
         Each question must contain the question, the variable name to save the question
         in a dictionary, the default_value and the test to verify the question"""
        self.questions.append((question, question_variable, verify_question, default_value))

    @staticmethod
    def ask_questions(question):
        """ Ask question to the manager. """
        return input(question)

    @staticmethod
    def display_responses(description_tournament):
        print(f"Vous venez de créer le tournoi suivant: \n"
              f"Nom du tournoi: {description_tournament.tournament_name}\n"
              f"Lieu du tournois: {description_tournament.tournament_place}\n"
              f"Dates: {description_tournament.date}")

    @staticmethod
    def display_tournament_in_progress(tournaments_in_progress):
        """ Display all the tournament in progress and ask a choice to the manager. """
        for key, value in tournaments_in_progress.items():
            print(f"{key}- {value['tournament_name']} à {value['tournament_place']} du "
                  f"{value['start_date']} au {value['end_date']}")
        return input("Entrez le numéro du tournoi que vous souhaitez reprendre :")

    @staticmethod
    def display_tournament_name(tournaments):
        """ Display a list of all the tournaments."""
        for tournament in tournaments:
            print(f"{tournament.tournament_name}, à {tournament.tournament_place}, {tournament.date}")

    @staticmethod
    def display_laps(tournament):
        """ Display all the laps of a tournament. """
        for lap in tournament.laps:
            print(f"nom: {lap.lap_name}")
            print(f"Début: {lap.datetime_start} ; Fin: {lap.datetime_end}")

    @staticmethod
    def display_matches(tournament):
        """ Display all the matches in a tournament. """
        for lap in tournament.laps:
            print(f"nom: {lap.lap_name}")
            for match in lap.matches:
                print(f"{match.opponents}: vainqueur: {match.winner}")
