class PlayerView:
    """ View to ask player information and send to Player"""
    def __init__(self):
        self.questions = []
        self.responses = {}
        self.verification = False

    def add_questions(self, question, question_variable, verify_question=""):
        """ Add questions to the manager to create a player.
         Each question must contain the question, the variable name to save the question
         in a dictionary, the default_value and the test to verify the question"""
        self.questions.append((question, question_variable, verify_question))

    @staticmethod
    def ask_questions(question):
        """ Ask questions to the manager in order to create a player. """
        return input(question)

    @staticmethod
    def display_informations(text):
        """ Display informations to the manager. """
        print(text)

    @staticmethod
    def display_informations_player():
        """ Display informations about a player. """
        print("Le joueur a été ajouté")

    @staticmethod
    def display_actors(actors):
        """ Display a list of all actors in the database. """
        for actor in actors:
            print(f"{actor.last_name} {actor.first_name} né(e) le {actor.birthday} (rang: {actor.ranking}.")
