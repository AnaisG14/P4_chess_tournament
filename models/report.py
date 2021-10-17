from tinydb import TinyDB
from operator import attrgetter
from models import player

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


    def list_actors(self, sort_methode="classement"):
        """ display all the actors of all tournament
        You can sort by name or by score."""
        self.actors = []
        db = TinyDB('db.json')
        players_table = db.table("players")
        serialized_actors = players_table.all()
        for actor in serialized_actors:
            first_name = actor['first_name']
            last_name = actor['last_name']
            birthday = actor['birthday']
            sexe = actor['sexe']
            ranking = int(actor['ranking'])
            self.actors.append(player.Player(first_name, last_name, birthday, sexe, ranking))

        if sort_methode == "name":
            self.actors.sort(key=attrgetter("last_name"))
            return self.actors
        else:
            self.actors.sort(key=attrgetter("ranking"))
            return self.actors

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

