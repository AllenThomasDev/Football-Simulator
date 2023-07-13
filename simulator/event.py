import random
import numpy as np

from simulator.configs.odds import odds, shot_outcome


class Event:
    def __init__(self, event, side, minute, player=None):
        self.event = event
        self.side = side
        self.minute = minute
        self.player = player

    def set_home_and_away_sides(self, home_side, away_side):
        self.sides = {home_side: "Home", away_side: "Away"}
        self.reverse = {home_side: away_side, away_side: home_side}

    def set_player_for_events(self, eventslist):
        position = random.choice(
            ["goalkeeper", "defenders", "midfielders", "attackers"]
        )
        players = list(eventslist[0].side.squad[position])
        player = random.choice(players)
        for e in eventslist:
            e.player = player
            if e.event == "Saved":
                e.player = e.side.squad["goalkeeper"][0]
        return eventslist

    def evaluate_event(self):
        if self.event == "Attempt":
            l = []
            l.append(Event(self.event, self.side, self.minute))
            attodds = []
            for oc in list(shot_outcome.keys()):
                attodds.append(shot_outcome[oc]["Probability"])
            att = random.choices(list(shot_outcome.keys()), attodds, k=1)[0]
            self.event = att
            l.append(Event(self.event, self.side, self.minute))
            if self.event == "On target":
                goalodds = []
                for g in list(shot_outcome["On target"]["is_goal"].values()):
                    goalodds.append(g)
                goal = random.choices(["Saved", "Goal"], goalodds, k=1)[0]
                if goal == "Saved":
                    self.side = self.reverse[self.side]
                self.event = goal
                l.append(Event(self.event, self.side, self.minute))
            l = self.set_player_for_events(l)
            return l
        elif self.event == "Foul":
            flist = []  # Foul handling below
            flist.append(Event("Foul", self.side, self.minute))
            flist.append(Event("Free kick won", self.reverse[self.side], self.minute))
            cardodds = []
            cardodds.append(
                odds[self.minute][self.sides[self.side]]["Events"]["Yellow card"]
                / odds[self.minute][self.sides[self.side]]["Events"]["Foul"]
            )
            cardodds.append(
                odds[self.minute][self.sides[self.side]]["Events"]["Red card"]
                / odds[self.minute][self.sides[self.side]]["Events"]["Foul"]
            )
            cardodds.append(1 - np.array(cardodds).sum())
            card = random.choices(["Yellow card", "Red card", "No card"], cardodds, k=1)[0]
            if card != "No card":
                flist.append(Event(card, self.side, self.minute))
            flist = self.set_player_for_events(flist)
            return flist
        else:
            l = []
            l.append(Event(self.event, self.side, self.minute))
            l = self.set_player_for_events(l)
            return l

    def show_event(self):
        print(str(self.minute) + "'", self.side.name, self.event, self.player.name)
