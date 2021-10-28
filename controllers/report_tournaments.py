from views import tournament_view
from controllers import management_tournament, home_menu_controller


class ReportTournament(management_tournament.ManagementTournament):
    """ Get and display all the tournaments saved in the database. """
    def __init__(self, option=""):
        """ Option is a string """
        super().__init__()
        self.view_report_tournament = tournament_view.TournamentView()
        self.option = option
        self.key = 1
        self.selected_tournament = None

    def __call__(self):
        if not self.option:
            self.view_report_tournament.display_tournament_name(self.all_tournaments)
            return home_menu_controller.HomeMenuController()
        else:
            self.selected_tournament = self.selecte_tournament()
            if self.selected_tournament:
                if self.option == "laps":
                    self.view_report_tournament.display_laps(self.selected_tournament)
                    return home_menu_controller.HomeMenuController()
                else:
                    self.view_report_tournament.display_matches(self.selected_tournament)
                    return home_menu_controller.HomeMenuController()
            else:
                self.view_report_tournament.display_information("\nAucun tournoi à afficher.")
                return home_menu_controller.HomeMenuController()
