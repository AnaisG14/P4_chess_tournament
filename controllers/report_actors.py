from models import list_actors_report
from views import view_report_list_player

class ReportActors:
    def __init__(self):
        self.report = list_actors_report.Report()
        self.actors = []
        self.display_report = view_report_list_player.ViewReportActors()

    def __call__(self):
        test_reponse = False
        while not test_reponse:
            response = self.display_report.ask_question("Selectionnez 1 pour un affichage par ordre "
                                                        "alphabétique ou 2 pour un affichage par classement")
            if response == "1":
                self.actors = self.report.list_actors("name")
                self.display_report.display_actors(self.actors)
                test_reponse = True
            elif response == "2":
                self.actors = self.report.list_actors()
                self.display_report.display_actors(self.actors)
                test_reponse = True
            else:
                print("Vous devez choisir 1 ou 2")


