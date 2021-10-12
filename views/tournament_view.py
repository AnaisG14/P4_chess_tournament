class TournamentView:
    """ User interface using tournament model """

    def __init__(self):
        self.questions = []
        self.verification = False

    def add_questions(self, question, question_variable, verify_question="", default_value=""):
        """ Add questions to the manager to create the tournament.
         Each question must contain the question, the variable name to save the question
         in a dictionnary, the default_value and the test to verify the question"""
        self.questions.append((question, question_variable, verify_question, default_value))

    def ask_questions(self, question):
        return input(question)

    def display_responses(self, description_tournament):
        print(f"Vous venez de créer le tournoi suivant: \n{description_tournament}")

