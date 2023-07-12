import random

import simulator.constants.managers as scm


class Manager:
    def __init__(self):
        self.name = random.choice(scm.names)
        self.formation = random.choice(scm.formations)
