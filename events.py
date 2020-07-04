from odds import odds
from odds import shot_outcome
import random
import numpy as np
class Event:
  def __init__(self,event,side,minute,players=None):
    self.event=event
    self.side=side
    self.minute=minute
    self.players=players
    

  def setSides(self,home_side,away_side):
    self.sides={home_side:'Home',away_side:'Away'}
    self.reverse={home_side:away_side,away_side:home_side}

  
  def setPlayer(self,eventslist):
    player=random.choice(list(eventslist[0].side.squad.keys()))
    for e in eventslist:
      e.players=player
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

