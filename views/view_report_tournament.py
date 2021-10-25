class ViewReportTournament:
    def __init__(self):
        pass

    def display_tournament_name(self, tournaments):
        for tournament in tournaments:
            print(f"{tournament.tournament_name}, à {tournament.tournament_place}, {tournament.date}")