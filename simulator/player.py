import pandas as pd
from tabulate import tabulate


class Player:
    facestats = [
        "short_name",
        "nationality",
        "overall",
        "player_positions",
        "team_position",
        "pace",
        "shooting",
        "passing",
        "dribbling",
        "defending",
        "physic",
    ]

    def __init__(self, row):
        self.stats = row.to_dict()
        self.stats["team_position"] = "Reserves"
        self.setPosition()

    def showPlayer(self):
        temp = pd.DataFrame(self.stats, index=[0])
        temp = temp.T
        temp = temp.dropna()
        print(tabulate(temp))

    def setPosition(self):
        if "B" in self.stats["player_positions"].split(",")[0]:
            self.stats["player_positions"] = "Defender"
        if "M" in self.stats["player_positions"].split(",")[0]:
            self.stats["player_positions"] = "Midfielder"
        for x in ["S", "F", "W"]:
            if x in self.stats["player_positions"].split(",")[0]:
                self.stats["player_positions"] = "Attacker"
