from operator import attrgetter
from models import player, tournament, management_tournament


class Report(management_tournament.ManagementTournament):
    """ affichage des éléments des tournois"""

    def __init__(self):
        """ tournament list is an insctance of TournamentList"""
        super().__init__()
        self.tournament_players = []

    def list_actors(self, sort_methode="classement"):
        """ display all the actors of all tournament
        You can sort by name or by score."""

        if sort_methode == "name":
            self.all_players.sort(key=attrgetter("last_name"))
            return self.all_players
        else:
            self.all_players.sort(key=attrgetter("ranking"))
            return self.all_players

    def list_tournament(self):
        """ Display all the tournament"""
        self.all_tournaments = self.get_tournaments()
        for tournament in self.all_tournaments:
            self.all_tournaments_name.append(tournament.tournament_name)
        return self.all_tournaments_name

    def list_players(self, tournament, sort_method="name"):
        """ display all the players of a tournament(an instance of TournamentModel)
        You can sort by name or by score."""
        self.tournament_players = []
        for player in tournament.players:
            self.tournament_players.append((player.last_name, player.score))
        if sort_method == "name":
            self.tournament_players.sort(key=attrgetter("last_name"))
            return self.tournament_players
        else:
            self.tournament_players.sort(key=attrgetter("ranking"))
            return self.tournament_players

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

