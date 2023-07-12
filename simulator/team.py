import numpy as np
import pandas as pd

from simulator.player import Player
from manager import Manager

df_player_data = pd.read_pickle("simulator/resources/player_data")

class Team:
    def __init__(self, team_name):
        self.players = {}
        self.squad = {}
        self.subs = {}
        self.reserves = {}
        self.team_name = team_name
        self.attackers = {}
        self.midfielders = {}
        self.defenders = {}
        self.goalkeepers = {}
        self.manager = Manager()
        self.addPlayers()
        self.populatePositions()
        self.playingSquad()
        self.attack = round(
            np.array(
                [
                    a.stats["overall"]
                    for a in self.players.values()
                    if a.stats["player_positions"] == "Attacker"
                    and (
                        a.stats["team_position"] == "Starter"
                        or a.stats["team_position"] == "Substitute"
                    )
                ]
            ).mean()
        )
        self.midfield = round(
            np.array(
                [
                    a.stats["overall"]
                    for a in self.players.values()
                    if a.stats["player_positions"] == "Midfielder"
                    and (
                        a.stats["team_position"] == "Starter"
                        or a.stats["team_position"] == "Substitute"
                    )
                ]
            ).mean()
        )
        self.defence = round(
            np.array(
                [
                    a.stats["overall"]
                    for a in self.players.values()
                    if (
                        a.stats["player_positions"] == "Defender"
                        or a.stats["player_positions"] == "GK"
                    )
                    and (
                        a.stats["team_position"] == "Starter"
                        or a.stats["team_position"] == "Substitute"
                    )
                ]
            ).mean()
        )

    def addPlayers(self):
        tdf = df_player_data[df_player_data["club"] == self.team_name]
        for index, row in tdf.iterrows():
            self.players[row["long_name"]] = Player(row)

    def populatePositions(self):
        for player in self.players.values():
            if player.stats["player_positions"] == "Attacker":
                self.attackers[player.stats["long_name"]] = player
            if player.stats["player_positions"] == "Defender":
                self.defenders[player.stats["long_name"]] = player
            if player.stats["player_positions"] == "Midfielder":
                self.midfielders[player.stats["long_name"]] = player
            if player.stats["player_positions"] == "GK":
                self.goalkeepers[player.stats["long_name"]] = player

    def playingSquad(self):
        [num_attackers, num_midfielders, num_defenders] = self.manager.formation
        squad = {}
        squad_attackers = {}
        squad_midfielders = {}
        squad_defenders = {}
        squad_gk = {}
        attackers = list(self.attackers.values())
        attackers.sort(key=lambda x: x.stats["overall"], reverse=True)
        for player in attackers[0 : num_attackers]:
            player.stats["team_position"] = "Starter"
            squad_attackers[player.stats["long_name"]] = player

        midfielders = list(self.midfielders.values())
        midfielders.sort(key=lambda x: x.stats["overall"], reverse=True)
        for player in midfielders[0 : num_midfielders]:
            player.stats["team_position"] = "Starter"
            squad_midfielders[player.stats["long_name"]] = player

        defenders = list(self.defenders.values())
        defenders.sort(key=lambda x: x.stats["overall"], reverse=True)
        for player in defenders[0 : num_defenders]:
            player.stats["team_position"] = "Starter"
            squad_defenders[player.stats["long_name"]] = player

        goalkeepers = list(self.goalkeepers.values())
        goalkeepers.sort(key=lambda x: x.stats["overall"], reverse=True)
        goalkeepers[0].stats["team_position"] = "Starter"
        squad_gk[goalkeepers[0].stats["long_name"]] = goalkeepers[0]
        squad.update(
            {
                "attackers": list(squad_attackers.values()),
                "midfielders": list(squad_midfielders.values()),
                "defenders": list(squad_defenders.values()),
                "goalkeeper": list(squad_gk.values()),
            }
        )
        self.squad = squad
