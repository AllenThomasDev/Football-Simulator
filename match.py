from odds import odds as odds
from odds import shot_outcome
import pprint as pp
import random
import copy
import numpy as np
import time
from tabulate import tabulate
from events import *

class Match:
    odds=odds
    reverse={'Home':'Away','Away':'Home'}
    eventkeys=list(odds[0]['Home']['Events'].keys())
    foulkeys=['Free kick won','Yellow card','Second yellow card','Red card']

    def __init__(self,home_side,away_side):
        self.odds=copy.deepcopy(odds)
        tlist=copy.deepcopy(Match.eventkeys)
        tlist.extend(['On target','Saved','Off target','Blocked','Hit the bar','Goal'])
        tside=dict(zip(tlist,[0]*len(tlist)))
        self.home_stats=dict(zip(tlist,[0]*len(tlist)))
        self.away_stats=dict(zip(tlist,[0]*len(tlist)))
        self.home_side=home_side
        self.away_side=away_side
        self.sides={home_side:'Home',away_side:'Away'}
        self.reverse={home_side:away_side,away_side:home_side}
        self.setOdds()
        self.matchevents=[]
        self.stats=dict(zip([self.home_side,self.away_side],[copy.copy(self.home_stats),copy.copy(self.away_stats)]))      
        self.home_players=home_side.players
        self.home_squad=home_side.squad
        self.away_players=away_side.players
        self.away_squad=away_side.squad
        self.events(home_side,away_side)
        
    
    def setOdds(self):
      haf=self.home_side.attack/self.away_side.defence
      aaf=self.away_side.attack/self.home_side.defence
      hdf=(self.home_side.defence**2*self.home_side.midfield)/(self.away_side.attack**2*self.away_side.midfield)
      adf=(self.away_side.defence**2*self.away_side.midfield)/(self.home_side.attack**2*self.home_side.midfield)
      for minute in range(100):
        self.odds[minute]['Home']['Events']['Attempt']=self.odds[minute]['Home']['Events']['Attempt']/(adf**2.33)
        self.odds[minute]['Away']['Events']['Attempt']=self.odds[minute]['Away']['Events']['Attempt']/(hdf**2.33)
     
      pass

    
    def events(self,home_side,away_side):
      for minute in range(100):
        for _ in range(135):                  
          if(random.uniform(0,1)<self.odds[minute]['Event']):
            plist=[]
            plist.append(self.odds[minute]['Home']['Probability'])
            plist.append(self.odds[minute]['Away']['Probability'])
            side = random.choices([self.home_side,self.away_side],plist)[0]
            event=random.choices(Match.eventkeys,list(self.odds[minute][self.sides[side]]['Events'].values()))[0]
            if event not in Match.foulkeys:
              e=Event(event,side,minute)
              e.setSides(home_side,away_side)
              self.addEvent(e)
        # if minute == 45:
          # self.showStats()
          # input('Press any key to start next half')


    def addEvent(self,event):
      for e in event.checkEvent():
        if e.event=='Substitution':
          if self.stats[e.side][e.event]<3:
            self.trackEvents(e)
        else:
          self.trackEvents(e)
        # self.showEvent(e)
        # time.sleep(0.01)
        self.matchevents.append(e)
    
    def trackEvents(self,event):
      if event.side == self.home_side:
        self.home_stats[event.event]=self.home_stats[event.event]+1
      else:
        self.away_stats[event.event]=self.away_stats[event.event]+1
      self.stats=dict(zip([self.home_side,self.away_side],[copy.copy(self.home_stats),copy.copy(self.away_stats)]))


    def showResult(self):
      self.home_goals=self.stats[self.home_side]['Goal']
      self.away_goals=self.stats[self.away_side]['Goal']
      if self.home_goals>self.away_goals:
        print(f"{self.home_side.team_name} won the match")
        print(f"Score {self.home_goals} - {self.away_goals}")
      elif self.away_goals>self.home_goals:
        print(f"{self.away_side.team_name} won the match")
        print(f"Score {self.home_goals} - {self.away_goals}")
      else:
        print(f"The match between {self.home_side.team_name} and {self.away_side.team_name} was a Draw")
        print(f"Score {self.home_goals} - {self.away_goals}")

    def Result(self):
      hg=self.stats[self.home_side]['Goal']
      ag=self.stats[self.away_side]['Goal']
      if hg==ag:
        return('Draw',self.home_side,self.away_side)
      elif hg>ag:
        return('Win',self.home_side,self.away_side)
      else:
        return('Win',self.away_side,self.home_side)

      pass
    def getGoals(self):
      return self.home_goals,self.away_goals

    def showStats(self):
      table=[]
      for stat in list(self.stats[self.home_side].keys()):
        l=[]
        l.append(stat)
        for team in [self.home_side,self.away_side]:
          l.extend([self.stats[team][stat]])
        table.append(l)
      print(tabulate(table,headers=['' ,self.home_side.team_name,self.away_side.team_name]))



    def showEvent(self,e):
      print(str(e.minute)+"'", e.side.team_name,e.event)
      
