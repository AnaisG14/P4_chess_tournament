from views import tournament_view
from controllers import management_tournament

class ReportTournament(management_tournament.ManagementTournament):
    def __init__(self, option=""):
        """ Option is a string """
        super().__init__()
        self.view_report_tournament = tournament_view.TournamentView()
        self.short_tournaments = []
        self.option = option
        self.key = 1
        self.selected_tournament = None

    def __call__(self):
        if not self.option:
            self.view_report_tournament.display_tournament_name(self.all_tournaments)
        else:
            self.selected_tournament = self.selecte_tournament()
            if self.option == "rounds":
                self.view_report_tournament.display_rounds(self.selected_tournament)
            else:
                self.view_report_tournament.display_matches(self.selected_tournament)



