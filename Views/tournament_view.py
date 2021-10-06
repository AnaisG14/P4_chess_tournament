class TournamentView:
    """ User interface using tournament model """

    def __init__(self):
        self.informations_tournament = {}
        self.questions = []
        self.responses = []
        self.verification = False

    def add_questions(self, question, question_variable, verify_question="", default_value=""):
        """ Add questions to the manager to create the tournament.
         Each question must contain the question, the variable name to save the question
         in a dictionnary, the default_value and the test to verify the question"""
        self.questions.append((question, question_variable, verify_question, default_value))

    def ask_questions(self, question):
        return input(question)

    def display_tournament(self):
        for key, value in self.informations_tournament.items():
            print(f"{key}: {value}")

    def __str__(self):
        return str(self.informations_tournament)