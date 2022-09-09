import numpy as np
import random
from simulator.constants.names import manager_names


class Manager():
    mindset = {'very defensive': [0.8, 1, 1.2, 1],
               'defensive': [0.9, 1, 1.1, 1],
               'balanced': [1, 1, 1, 1],
               'attacking': [1.1, 1, 0.9, 1],
               'very attacking': [1.2, 1, 0.8, 1]}
    ivchart = {1: -2, 2: -1, 3: 0, 4: 1, 5: +2}
    base = [10, 10, 10]
    sd = [5, 5, 5]

    def __init__(self):
        self.ivs = np.random.randint(1, 6, 3)
        self.name = manager_names[random.randint(0, 99)]
        self.set_stats()

    def set_stats(self):
        self.managing = int(np.floor(max(min(np.random.normal(
            Manager.base[0], Manager.sd[0], 1) + Manager.ivchart[self.ivs[0]], 20), 0)))
        self.training = int(np.floor(max(min(np.random.normal(
            Manager.base[1], Manager.sd[1], 1) + Manager.ivchart[self.ivs[1]], 20), 0)))
        self.scouting = int(np.floor(max(min(np.random.normal(
            Manager.base[2], Manager.sd[2], 1) + Manager.ivchart[self.ivs[2]], 20), 0)))
        self.stats = np.array([self.managing, self.training, self.scouting])
        self.defenders = min(
            max(2, round(float(np.random.normal(4, 0.4, 1)))), 5)
        self.strikers = min(
            max(1, round(float(np.random.normal(2, 0.7, 1)))), 3)
        self.midfielders = 10 - self.defenders - self.strikers
        self.formation = np.array(
            [self.defenders, self.midfielders, self.strikers])
