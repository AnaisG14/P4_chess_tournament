class TournamentView:
    """ User interface using tournament model """

    def __init__(self):
        self.informations_tournament = {}
        self.questions = []
        self.responses = []
        self.verification = False

    def add_questions(self, question, question_variable, verify_question=""):
        """ Add questions to the manager to create the tournament """
        self.questions.append((question, question_variable, verify_question))

    def ask_questions(self):
        for question in self.questions:
            self.verification = False
            while self.verification == False:
                response = input(question[0])
                self.verify_response(question, response)

    def verify_response(self, question, response):
        """ verify response before save it in the dictionnary """
        if question[2]:
            condition = question[2]
            print(condition)
            if f"{condition}":
                self.informations_tournament[question[1]] = response
                self.verification = True
        else:
            self.informations_tournament[question[1]] = response
            self.verification = True

    def __str__(self):
        return str(self.informations_tournament)