from names import *
import random
import numpy as np
class Player:
    def __init__(self,row):
        self.shooting=row['shooting']
        self.defending=row['defending']
        self.passing=row['passing']
        self.pace=row['pace']
        self.physical=row['physic']
        self.dribbling=row['dribbling']
        self.name=row['long_name']
        self.overall=row['overall']
        self.nationality=row['nationality']
        self.value=row['value_eur']
        self.club=row['club']
        self.position=row['player_positions']
        self.setPosition()
        self.team_position='Reserves'

    def setPosition(self):
        if 'B' in self.position.split(",")[0]:
            self.position='Defender'
        if 'M' in self.position.split(",")[0]:
            self.position='Midfielder'
        for x in ['S','F','W']:
            if x in self.position.split(",")[0]:
                self.position='Attacker'
        
        pass
