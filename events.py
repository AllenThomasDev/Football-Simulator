from odds import odds as odds
from odds import shot_outcome
from odds import goal_distribution
import random
import match as m
import numpy as np
class Event:
  def __init__(self,event,side,minute,player=None):
    self.event=event
    self.side=side
    self.minute=minute
    self.player=player
    

  def setSides(self,home_side,away_side):
    self.sides={home_side:'Home',away_side:'Away'}
    self.reverse={home_side:away_side,away_side:home_side}

  
  def setPlayer(self,eventslist):
    position=random.choices(['goalkeeper','defenders','midfielders','attackers'])[0]
    if eventslist[0].event=='Attempt':
      position=random.choices(['goalkeeper','defenders','midfielders','attackers'],list(goal_distribution.values()))[0]
    players=list(eventslist[0].side.squad[position].values())
    odds=[x.stats['shooting'] for x in players]
    player=random.choices(players,odds)[0]
    for e in eventslist:
      e.player=player
    return eventslist
    pass


  def checkEvent(self):
    side=self.side
    if self.event=='Attempt':
      l=[]
      l.append(Event(self.event,self.side,self.minute))
      attodds=[]
      for oc in list(shot_outcome.keys()):
        attodds.append(shot_outcome[oc]['Probability'])
      att=random.choices(list(shot_outcome.keys()),attodds)[0]
      self.event=att
      l.append(Event(self.event,self.side,self.minute))
      if self.event=='On target':
        goalodds=[]
        for g in list(shot_outcome['On target']['is_goal'].values()):
          goalodds.append(g)
        goal=random.choices(['Saved','Goal'],goalodds)[0]
        self.event=goal
        l.append(Event(self.event,self.side,self.minute))
      l=self.setPlayer(l)
      return l
    elif self.event=='Foul':
      flist=[]                       #Foul handling below
      flist.append(Event('Foul',self.side,self.minute))
      flist.append(Event('Free kick won',self.reverse[self.side],self.minute))
      cardodds=[]
      cardodds.append(odds[self.minute][self.sides[self.side]]['Events']['Yellow card']/odds[self.minute][self.sides[self.side]]['Events']['Foul'])
      cardodds.append(odds[self.minute][self.sides[self.side]]['Events']['Red card']/odds[self.minute][self.sides[self.side]]['Events']['Foul'])
      cardodds.append(1-np.array(cardodds).sum())
      card=random.choices(['Yellow card','Red card','No card'],cardodds)[0]
      if card != 'No card':
        flist.append(Event(card,self.side,self.minute))
      flist=self.setPlayer(flist)
      return flist
    else:
      l=[]
      l.append(Event(self.event,self.side,self.minute))
      l=self.setPlayer(l)
      return l

