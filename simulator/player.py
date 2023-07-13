class Player:
    # Positions:
    ATTACKER = "attacker"
    MIDFIELDER = "midfielder"
    DEFENDER = "defender"
    GOALKEEPER = "goalkeeper"

    # TEAM STATUS:
    STARTER = "starter"
    SUBSTITUTE = "substitute"
    RESERVE = "reserve"

    GOALKEEPER_ATTRIBUTES = [
        "gk_diving",
        "gk_handling",
        "gk_kicking",
        "gk_reflexes",
        "gk_speed",
        "gk_positioning",
    ]

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
        self.keeping = 0
        self.team_status = Player.RESERVE
        self.position = stats["player_positions"]
        self.set_player_position(stats["player_positions"])
        self.set_goalkeeper_rating(stats)

    def set_player_position(self, player_positions):
        main_position = player_positions.split(",")[0]
        if "B" in main_position:
            self.position = Player.DEFENDER
        elif "M" in main_position:
            self.position = Player.MIDFIELDER
        elif ("S" in main_position) or ("F" in main_position) or ("W" in main_position):
            self.position = Player.ATTACKER
        else:
            self.position = Player.GOALKEEPER

    def set_goalkeeper_rating(self, stats):
        if self.is_goalkeeper():
            gk_rating = 0
            for attribute in Player.GOALKEEPER_ATTRIBUTES:
                gk_rating += stats[attribute]
            self.keeping = gk_rating // len(Player.GOALKEEPER_ATTRIBUTES)

    def is_attacker(self):
        return self.position == Player.ATTACKER

    def is_midfielder(self):
        return self.position == Player.MIDFIELDER

    def is_defender(self):
        return self.position == Player.DEFENDER

    def is_goalkeeper(self):
        return self.position == Player.GOALKEEPER

    def set_as_starter(self):
        self.position = Player.STARTER

    def is_starter(self):
        return self.position == Player.STARTER
