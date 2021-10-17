class ViewReportActors:
    def __init__(self):
        pass

    def ask_question(self, question):
        response = input(question)
        return response

    def display_actors(self, actors):
        for actor in actors:
            print(actor)