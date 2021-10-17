from models import tournament, round, match

class Deserialisation:
    def __init__(self, serialized_tounnament):
        self.serialized_tournament = serialized_tounnament
        self.serialized_round = ""
        self.serialized_match = ""
        self.serialized_player = ""
        self.recreate_tournament = ""
        self.recreate_round = ""
        self.recreate_match = ""
        self.recreate_player = ""

    def deserialized_player(self, serialised_player):
        first_name = serialized_player['first_name']
        last_name = serialized_player['last_name']
        birthday = serialized_player['birthday']
        sexe = serialized_player['sexe']
        ranking = serialized_player['ranking']
        return {'first_name': first_name, 'last_name': last_name, 'birthday': birthday, 'sexe': sexe, 'ranking': ranking}

    def deserialized_tournament(self):
        tournament_name = self.serialized_tournament['tournament_name']
        tournament_place = self.serialized_tournament['tournament_place']
        rounds_number = self.serialized_tournament['rounds_number']
        time_controller = self.serialized_tournament['time_controller']
        manager_description = self.serialized_tournament['manager_description']
        start_date = self.serialized_tournament['start_date']
        end_date = self.serialized_tournament['end_date']
        informations_tournament = {'tournament_name': tournament_name,
                                   'tournament_place':tournament_place,
                                   'rounds_number': rounds_number,
                                   'time_controller': time_controller,
                                   'manager_description': manager_description,
                                   'start_date': start_date,
                                   'end_date': end_date
                                   }

        self.recreate_tournament = tournament.Tournament(**informations_tournament)
        rounds_name = self.serialized_tournament['rounds_name']
        for rounds in rounds_name:
            deserialized_round = self.deserialized_round(rounds)
            self.recreate_tournament.rounds.append(deserialized_round)
        players = self.serialized_tournament['players']
        for player in players:
            deserialized_player = self.deserialized_player(player)
            self.recreate_tournament.players.append(deserialized_player)

        self.recreate_tournament.results = serialized_tournament['result']
        return self.recreate_tournament

    def deserialized_round(self, serialized_round):
        round_name = serialized_round['round_name']
        self.recreate_round = round.Round(self.recreate_tournament.tournament_name, round_name)

        round_players = serialized_round['round_players']
        for player in round_players:
            deserialized_player = self.deserialized_player(player)
            self.recreate_round.round_players.append(deserialized_player)
        matches = serialized_round['match']
        for serialized_match in matches:
            deserialized_match = self.deserialized_match(serialized_match)
            self.recreate_round.matches.append(deserialized_match)
        self.recreate_round.datetime_start = serialised_round['datetime_start']
        self.recreate_round.datetime_end = serialised_round['datetime_end']
        return self.recreate_round

    def deserialized_match(self, serialized_match):
        player1 = self.deserialized_player(serialized_match['player1'])
        player2 = self.deserialized_player(serialized_match['player2'])
        self.recreate_match = match.Match(player1, player2)
        self.recreate_match.match = (player1, player2)
        return self.recreate_match




