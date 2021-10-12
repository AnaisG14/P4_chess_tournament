class PlayerView:
    """ View to ask player information and send to Player"""
    def __init__(self):
        self.questions = []
        self.responses = {}
        self.verification = False

    def add_questions(self, question, question_variable, verify_question=""):
        """ Add questions to the manager to create a player.
         Each question must contain the question, the variable name to save the question
         in a dictionnary, the default_value and the test to verify the question"""
        self.questions.append((question, question_variable, verify_question))

    def ask_questions(self, question):
        return input(question)

    def display_informations(self, text):
        print(text)

    def display_informations_player(self):
        print("Le joueur suivant a été ajouté")
        for value in self.responses.values():
            print(f"{value}\n")

