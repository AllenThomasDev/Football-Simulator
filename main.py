import time as time
import players as p
import teams as t
import leagues as l 
import match as m

pl=l.League()
# # pl.showLeague()
for _ in range(38):
    pl.simWeek()
    pl.showStandings()
print('Final Standings are -')
pl.showStandings()
