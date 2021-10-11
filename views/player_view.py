class PlayerView:
    """ View to ask player information and send to Player"""
    def __init__(self):
        self.informations_player = {}
        self.questions = []

    def add_questions(self, question, question_variable, verify_question=""):
        """ Add questions to the manager to create a player.
         Each question must contain the question, the variable name to save the question
         in a dictionnary, the default_value and the test to verify the question"""
        self.questions.append((question, question_variable, verify_question))

    def ask_questions(self, question):
        return input(question)

    def display_informations(self, text):
        print(text)

    def __str__(self):
        return (self.informations_player)

    def __repr__(self):
        for key, value in self.informations_player.items():
            print(f"{key}: {value}")