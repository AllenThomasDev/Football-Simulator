# Football-League-Simulator

You can use this project to simulate different football leagues from across the world using FIFA 20 stats.

When you run main.py, matches between all the teams will be simulated week by week and the final output will look similar to this - 
|    | Club          |   Matches Played |   Wins |   Draws |   Losses |   Points |   GF |   GA |   GD |
|----|---------------|------------------|--------|---------|----------|----------|------|------|------|
|  1 | Juventus      |               38 |     31 |       1 |        6 |       94 |  113 |   32 |   81 |
|  2 | Napoli        |               38 |     26 |       6 |        6 |       84 |   83 |   31 |   52 |
|  3 | Inter         |               38 |     26 |       5 |        7 |       83 |   93 |   45 |   48 |
|  4 | Milan         |               38 |     23 |      10 |        5 |       79 |   68 |   25 |   43 |
|  5 | Lazio         |               38 |     20 |       7 |       11 |       67 |   82 |   57 |   25 |
|  6 | Torino        |               38 |     17 |       7 |       14 |       58 |   59 |   45 |   14 |
....

___ 

I have used a probalistic approach to simulate the events of the match-
For every minute in a match, the probability of a particular event occurring was calculated. The probabilities are then scaled according to the strengths of the teams and the match is simulated minute by minute.

eg. The probabilities of different events for the 72nd minute -
```python
 72: {'Away': {'Events': {'Attempt': 0.21580320536712636,
                          'Corner': 0.07957510249720462,
                          'Failed through ball': 0.03745806932538204,
                          'Foul': 0.23108460678345136,
                          'Free kick won': 0.23518449496831906,
                          'Hand ball': 0.01360417443160641,
                          'Key Pass': 0.15933656354826686,
                          'Offside': 0.03745806932538204,
                          'Own goal': 0.0003727171077152441,
                          'Penalty conceded': 0.0018635855385762206,
                          'Red card': 0.002422661200149087,
                          'Second yellow card': 0.0,
                          'Sending off': 0.0039135296310100634,
                          'Substitution': 0.1334327245620574,
                          'Yellow card': 0.049571375326127466},
               'Probability': 0.48569876900796527},
      'Event': 0.011740589091071393,
      'Home': {'Events':{....}}}
```

> Such probabilities have been calculated for each minute from 0 to 100. 
> One or more events may occur in a single minute
As of 14/06/2020 

Top 5 Leagues are natively supported -
* English Premier League 
* La Liga
* Seria A
* Bundesliga 
* Ligue 1
#### Note: You can set up your own league by editing teams in odds.py and adding an option in main.py. Ensure that you use the correct name. eg. 'Man Utd' will not work , you will have to use 'Manchester United' because that is how it is stored. To see the list of valid team names, you can add 
```python
print(df['club'].unique())
#to playerlist.py and run it seperately
```
```python
league_options={'spain': {'name': 'La Liga Santander',
  'teams': ['Real Madrid',
   'FC Barcelona',
   'Valencia CF',
   'Atlético Madrid',
   'RC Celta',
   'Real Betis',
   'Villarreal CF',
   'Real Sociedad',
   'Athletic Club de Bilbao',
   'Deportivo Alavés',
   'Getafe CF',
   'Sevilla FC',
   'Levante UD',
   'Granada CF',
   'CA Osasuna',
   'Real Valladolid CF',
   'RCD Espanyol',
   'SD Eibar',
   'RCD Mallorca',
   'CD Leganés']},
   ....
   ```
   >You can use your own custom list of teams and league name. There is no theoretical limit to the number of teams, but try to limit the number of teams to 100 and ideally try to have an even number of teams.


Currently simMatch() will simulate the match in its entirety and update the league table. But there are functions that can be used to see the timeline of a match as it happens. In future builds, the user will be able to take charge of a particular team and see the events of any game that he is involved in live. 


```
You will need to install packages specified in requirements.txt, you can do this by -
pip install -r requirements.txt
```

Please feel free to play around with the code and let me know if you find any issues or you need some help with certain functions

You can contact me at allen.thomas.dev@gmail.com
