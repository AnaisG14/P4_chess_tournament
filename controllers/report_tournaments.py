from models import tournaments_reports
from views import view_report_tournament

class ReportTournament:
    def __init__(self):
        self.report_tournament_model = tournaments_reports.ReportTournament()
        self.report_tournament_view = view_report_tournament.ViewReportTournament()
        self.short_tournaments = []

    def __call__(self):
        self.report_tournament_view.display_tournament_name(self.report_tournament_model.all_tournaments)


