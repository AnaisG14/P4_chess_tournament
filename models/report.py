class Report:
    """ affichage des éléments des tournois"""

    def __init__(self):
        """ tournament list is an insctance of TournamentList"""
        self.all_tournaments = []
        self.actors = []
        self.tournament_players = []
        self.all_tournaments_name = []
        self.rounds_per_tournament = []
        self.matches_tournament = []

    def add_tournament(self, tournament):
        self.all_tournaments.append(tournament)


    def list_actors(self, sort_methode="score"):
        """ display all the actors of all tournament
        You can sort by name or by score."""
        self.actors = []
        for tournament in self.all_tournaments:
            for actor in tournament.players:
                self.actors.append((actor.last_name, actor.ranking))
        if sort_methode == "name":
            self.actors.sort(key=lambda x: x[0])
            return self.actors
        else:
            self.actors.sort(key=lambda x: x[1])
            return self.actors

    def list_players(self, tournament, sort_method="name"):
        """ display all the players of a tournament(an instance of TournamentModel)
        You can sort by name or by score."""
        self.tournament_players = []
        for player in tournament.players:
            self.tournament_players.append((player.last_name, player.score))
        if sort_method == "name":
            self.tournament_players.sort(key=lambda x: x[0])
            return self.tournament_players
        else:
            self.tournament_players.sort(key=lambda x: x[1])
            return self.tournament_players

    def list_tournament(self):
        """ Display all the tournament"""
        for tournament in self.all_tournaments:
            self.all_tournaments_name.append(tournament.tournament_name)
        return self.all_tournaments_name

    def list_rounds(self, tournament):
        """ dipslay all the rounds of tournament (an instance of TournamentModel)"""
        for round in tournament.rounds:
            self.rounds_per_tournament.append(round)
        return self.rounds_per_tournament

    def list_matches(self, tournament):
        """ diplay all the matches of tournament (an instance of TournamentModel"""
        for round in tournament.rounds:
            self.matches_tournament.append(round.matches)
        return self.matches_tournament

    # def __str__(self):
    #     return str(self.actors)

