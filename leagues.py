from teams import *
import random
import time
import match as m
import pandas as pd
from odds import *
from fuzzywuzzy import fuzz
from itertools import permutations
import copy
import pprint
class League:
    country={1:'spain',2:'england',3:'germany',4:'italy',5:'france'}
    def __init__(self,option):
        self.players={}
        self.teams={}
        self.leaguename=league_options[League.country[option]]['name']
        self.names=league_options[League.country[option]]['teams']  #self.names=names of the teams . will be changed soon 13/06/2020
        self.setTeams()
        self.setPlayers()
        self.schedule=self.create_balanced_round_robin(self.names)
        self.week=0
        self.standings=self.initTable()


    def initTable(self):
        table=pd.DataFrame(columns=['Club','Matches Played','Wins','Draws','Losses','Points','GF','GA','GD'])
        for team in self.names:
            row=pd.DataFrame([[team,0,0,0,0,0,0,0,0]],columns=['Club','Matches Played','Wins','Draws','Losses','Points','GF','GA','GD'])
            table=table.append(row)
        table=table.reset_index(drop=True)
        table.index=table.index+1
        return table


    def showStandings(self):
        print(tabulate(self.standings,headers=self.standings.columns,tablefmt='github'))


    def setTeams(self):
        for team in self.names:
            t=Team(team)
            self.teams[team]=t
    
    def searchTeam(self):
        query=input("\nEnter the name of the team you want to search\n")
        for team in self.teams.keys():
            Partial_Ratio = fuzz.partial_ratio(query.lower(),team.lower())
            if Partial_Ratio>90:
                self.teams[team].showTeam()

    def searchPlayer(self):
        query=input("\nEnter the name of the player you want to search\n")
        for player in self.players.keys():
            Partial_Ratio = fuzz.partial_ratio(query.lower(),player.lower())
            if Partial_Ratio>90:
                self.players[player].showPlayer()

    def showPlayers(self,position=['striker','midfielder','defender','goalkeeper']):
        df=pd.DataFrame()
        for team in self.teams.values():
            df=df.append(team.getPlayers(position=position))
        df.columns=['Name','Position','Stats','IVs']
        print(tabulate(df))

    def setPlayers(self):
        for team in self.teams.values():
            self.players.update(team.players)

    def showLeague(self):
        for team in self.teams.values():
            team.showTeam()
    pass

    def simMatch(self,home_team_name,away_team_name):
        home_team=self.teams[home_team_name]
        away_team=self.teams[away_team_name]
        match=m.Match(home_team,away_team)
        # match.showResult()
        self.updateTable(match)
        pass

    def updateTable(self,match):
        (result,winner,loser)=match.Result()
        table=self.standings
        winnergoals=match.stats[winner]['Goal']
        losergoals=match.stats[loser]['Goal']
        dif=winnergoals-losergoals
        if result=='Draw':
            for team in [winner,loser]:
                table.loc[(table['Club']==team.team_name)]+=['',1,0,1,0,1,winnergoals,losergoals,0]
        else:
            table.loc[(table['Club']==winner.team_name)]+=['',1,1,0,0,3,winnergoals,losergoals,dif]
            table.loc[(table['Club']==loser.team_name)]+=['',1,0,0,1,0,losergoals,winnergoals,-dif]
        pass
        table=table.sort_values(by=['Points','GD','GF'],ascending=False)
        table=table.reset_index(drop=True)
        table.index=table.index+1
        self.standings=table

    def simLeague(self):
        while self.week<len(self.schedule):
            self.simWeek()
            self.showStandings()
        pass

    
    def simWeek(self):
        for h,a in self.schedule[self.week]:
            self.simMatch(h,a)
        self.week+=1
        pass
    def create_balanced_round_robin(self,teams):
        """ Create a schedule for the players in the list and return it"""
        s = []
        if len(teams) % 2 == 1: teams = teams + [None]
        # manipulate map (array of indexes for list) instead of list itself
        # this takes advantage of even/odd indexes to determine home vs. away
        n = len(teams)
        map = list(range(n))
        mid = n // 2
        for i in range(n-1):
            l1 = map[:mid]
            l2 = map[mid:]
            l2.reverse()
            round = []
            for j in range(mid):
                t1 = teams[l1[j]]
                t2 = teams[l2[j]]
                if j == 0 and i % 2 == 1:
                    # flip the first match only, every other round
                    # (this is because the first match always involves the last player in the list)
                    round.append((t2, t1))
                else:
                    round.append((t1, t2))
            s.append(round)
            # rotate list by n/2, leaving last element at the end
            map = map[mid:-1] + map[:mid] + map[-1:]
        temp=copy.copy(s)
        for item in temp:
            l=[]
            for x in item:
                l.append(x[::-1])
            s.append(l)
        return s

