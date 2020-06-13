import pprint as pp
import players as p
from manager import *
from names import gen_name
import numpy as np
import random
import pandas as pd
from playerlist import df
from tabulate import tabulate

class Team:
    attlist=['name','nationality', 'overall', 'position','team_position', 'pace','shooting', 'passing', 'dribbling', 'defending', 'physical']
    def __init__(self,team_name):
        self.players={}
        self.squad={}
        self.subs={}
        self.reserves={}
        self.team_name=team_name
        self.addPlayers()
        self.attackers={}
        self.midfielders={}
        self.defenders={}
        self.goalkeepers={}   
        self.populatePositions()
        self.manager=None
        self.setManager()
        self.playingSquad()
        self.attack=round(np.array([a.overall for a in self.players.values() if a.position=='Attacker' and (a.team_position=='Starter' or a.team_position=='Substitute')]).mean())
        self.midfield=round(np.array([a.overall for a in self.players.values() if a.position=='Midfielder' and (a.team_position=='Starter' or a.team_position=='Substitute')]).mean())
        self.defence=round(np.array([a.overall for a in self.players.values() if (a.position=='Defender' or a.position=='GK') and (a.team_position=='Starter' or a.team_position=='Substitute')]).mean())
        # self.playingSquad()

    def addPlayers(self):
        tdf=df[df['club']==self.team_name]
        for index, row in tdf.iterrows():
            self.players[row['long_name']]=p.Player(row)
            pass



    def setManager(self):
        self.manager=Manager()

    def showPlayers(self,player_dict=None):
        if player_dict==None:
            player_dict=self.players
        pl=[]
        df=pd.DataFrame()
        i=1
        for player in player_dict.values():
            temp=pd.DataFrame.from_records(player.__dict__,index=[i],columns=Team.attlist)
            df=df.append(temp)
            i+=1
        print(tabulate(df,headers=[c.capitalize() for c in df.columns],tablefmt='psql',stralign='left'))
            
    
    def populatePositions(self):
        for player in self.players.values():
            if player.position =='Attacker':
                self.attackers[player.name]=player
            if player.position =='Defender':
                self.defenders[player.name]=player
            if player.position =='Midfielder':
                self.midfielders[player.name]=player
            if player.position =='GK':
                self.goalkeepers[player.name]=player

    def showManager(self):
        table_data=[]
        table_data.append([self.manager.name,'Manager',self.manager.stats,self.manager.ivs,self.manager.formation])
        print(tabulate(table_data))

    def showTeam(self,player_dict=None,position=['striker','midfielder','defender','goalkeeper']):
        self.Substitutes()
        self.showPlayers()
        self.showPlayers(player_dict=self.squad)
        self.showStats()
        self.showManager()


    def showStats(self):
        print(f"{self.team_name}'s Stats\nAttack = {self.attack}\nMidfield = {self.midfield}\nDefence = {self.defence}")
    def playingSquad(self):
        squad={}
        attackers=list(self.attackers.values())
        attackers.sort(key = lambda x:x.overall,reverse=True)
        for player in attackers[0:self.manager.strikers]:
            player.team_position='Starter'
            squad[player.name]=player

        midfielders=list(self.midfielders.values())
        midfielders.sort(key = lambda x:x.overall,reverse=True)
        for player in midfielders[0:self.manager.midfielders]:
            player.team_position='Starter'
            squad[player.name]=player

        defenders=list(self.defenders.values())
        defenders.sort(key = lambda x:x.overall,reverse=True)
        for player in defenders[0:self.manager.defenders]:
            player.team_position='Starter'
            squad[player.name]=player

        goalkeepers=list(self.goalkeepers.values())
        goalkeepers.sort(key = lambda x:x.overall,reverse=True)
        goalkeepers[0].team_position='Starter'
        squad[goalkeepers[0].name]=goalkeepers[0]
        self.squad=squad

    def Substitutes(self):
        subs=[x for x in self.players.keys() if x not in self.squad.keys()][:7]
        for player in subs:
            self.players[player].team_position='Substitute'
            self.subs[player]=self.players[player]
        reserves = [r for r in self.players.items() if (r not in self.squad.items() and r not in self.subs.items())]
        self.reserves.update(reserves)
        pass
