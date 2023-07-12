import pandas as pd

from simulator.player import Player
from manager import Manager

df_players_data = pd.read_pickle("simulator/resources/player_data")

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.manager = Manager()
        self.players = {}
        self.squad = {}
        self.attack = 0
        self.midfield = 0
        self.defence = 0
        self.set_players()
        self.set_stats()
        self.set_squad()

    def set_players(self):
        df_team_players_data = df_players_data[df_players_data["club"] == self.name]
        for index, df_player in df_team_players_data.iterrows():
            self.players[df_player["long_name"]] = Player(df_player)

    def set_stats(self):
        self.attackers = [
            player for player in self.players.values() if player.is_attacker()
        ]
        self.defenders = [
            player for player in self.players.values() if player.is_defender()
        ]
        self.midfielders = [
            player for player in self.players.values() if player.is_midfielder()
        ]
        self.goalkeepers = [
            player for player in self.players.values() if player.is_goalkeeper()
        ]
        self.attack = sum(player.overall for player in self.attackers) / len(
            self.attackers
        )
        self.defence = (
            sum(player.overall for player in self.defenders)
            + sum(player.overall for player in self.goalkeepers)
        ) / (len(self.defenders) + len(self.goalkeepers))
        self.midfield = sum(player.overall for player in self.midfielders) / len(
            self.midfielders
        )

    def set_squad(self):
        [num_attackers, num_midfielders, num_defenders] = self.manager.formation
        squad_attackers = []
        squad_midfielders = []
        squad_defenders = []

        self.attackers.sort(key=lambda x: x.overall, reverse=True)
        for player in self.attackers[0:num_attackers]:
            player.set_as_starter()
            squad_attackers.append(player)

        self.midfielders.sort(key=lambda x: x.overall, reverse=True)
        for player in self.midfielders[0:num_midfielders]:
            player.set_as_starter()
            squad_midfielders.append(player)

        self.defenders.sort(key=lambda x: x.overall, reverse=True)
        for player in self.defenders[0:num_defenders]:
            player.set_as_starter()
            squad_defenders.append(player)

        self.goalkeepers.sort(key=lambda x: x.overall, reverse=True)
        player = self.goalkeepers[0]
        player.set_as_starter()
        squad_gk = [player]
        self.squad = {
            "attackers": squad_attackers,
            "midfielders": squad_attackers,
            "defenders": squad_defenders,
            "goalkeeper": squad_gk,
        }
