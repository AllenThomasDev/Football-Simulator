import time as time
import players as p
import teams as t
import leagues as l 
import match as m


print('Welcome to my League Simulator\n You can use my project to simulate Football Leagues across the world\n Please enter the league you would like to simulate-')
n=0
while n not in ['1','2','3','4','5']:    
    print("""
    1 - La Liga Santander
    2 - Premier League
    3 - Bundesliga
    4 - Seria A
    5 - Ligue 1""")
    n=input()
    if n not in ['1','2','3','4','5']:
        print('Enter a Valid input')
pl=l.League(int(n))
pl.simLeague()
print('Final Standings are -')
pl.showStandings()