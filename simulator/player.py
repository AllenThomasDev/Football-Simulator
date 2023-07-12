class Player:
    def __init__(self, df_player):
        stats = df_player.to_dict()
        self.name = stats["short_name"]
        self.nationality = stats["nationality"]
        self.overall = stats["overall"]
        self.pace = stats["pace"]
        self.shooting = stats["shooting"]
        self.passing = stats["passing"]
        self.dribbling = stats["dribbling"]
        self.defending = stats["defending"]
        self.physic = stats["physic"]
        self.position = stats["player_positions"]
        self.set_player_position(stats["player_positions"])
        self.team_status = "Reserves"

    def set_player_position(self, player_positions):
        main_position = player_positions.split(",")[0]
        if "B" in main_position:
            self.position = "Defender"
        elif "M" in main_position:
            self.position = "Midfielder"
        elif ("S" in main_position) or ("F" in main_position) or ("W" in main_position):
            self.position = "Attacker"
        else:
            self.position = "Goalkeeper"

    def is_attacker(self):
        return self.position == "Attacker"

    def is_midfielder(self):
        return self.position == "Midfielder"

    def is_defender(self):
        return self.position == "Defender"

    def is_goalkeeper(self):
        return self.position == "Goalkeeper"

    def set_as_starter(self):
        return self.position == "Starter"

    def is_starter(self):
        return self.position == "Starter"
