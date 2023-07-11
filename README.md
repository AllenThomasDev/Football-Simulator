# Football-League-Simulator

This Python project enables you to simulate various football leagues from around the world using FIFA 20 stats.
The simulator runs week-by-week simulations of matches between all teams in the selected league, resulting in a final output that look something like this:

|    | Club          |   Matches Played |   Wins |   Draws |   Losses |   Points |   GF |   GA |   GD |
|----|---------------|------------------|--------|---------|----------|----------|------|------|------|
|  1 | Juventus      |               38 |     31 |       1 |        6 |       94 |  113 |   32 |   81 |
|  2 | Napoli        |               38 |     26 |       6 |        6 |       84 |   83 |   31 |   52 |
|  3 | Inter         |               38 |     26 |       5 |        7 |       83 |   93 |   45 |   48 |
|  4 | Milan         |               38 |     23 |      10 |        5 |       79 |   68 |   25 |   43 |
|  5 | Lazio         |               38 |     20 |       7 |       11 |       67 |   82 |   57 |   25 |
|  6 | Torino        |               38 |     17 |       7 |       14 |       58 |   59 |   45 |   14 |
....

## How to run the simulator

To run this simulator locally, you need to perform the following steps:

1. Clone this repositor on your local machine:

```bash
git clone https://github.com/AllenThomasDev/Football-Simulator.git
```

2. Move inside the main project directory:

```bash
cd Football-Simulator
```

3. Setup and activate your virtual environment (optional):

```bash
# To create a virtual env:
python -m venv .venv

# For activation use one of the following commands based on your OS:
source env/bin/activate   # On Mac / Linux
env/Scripts/activate.bat  # In Windows CMD
env/Scripts/Activate.ps1  # In Windows Powershel
```

4. Install the required packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

5. Start the simulator by running: `python simulator`

## How does it work

The simulator employs a probabilistic approach to simulate match events. The probabilities of different events occurring in a match are calculated minute by minute. These probabilities are then scaled based on the strengths of the teams, and the match is simulated.

For example, the probabilities of different events for the 72nd minute:

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

_Such probabilities have been calculated for each minute from 0 to 100.</br>_
_As of 14/06/2020 one or more events may occur in a single minute._

```python
leagues = {
    "spain": {
        "name": "La Liga Santander",
        "teams": [
            "Real Madrid",
            "FC Barcelona",
            "Valencia CF",
            "Atlético Madrid",
            "RC Celta",
            "Real Betis",
            "Villarreal CF",
            "Real Sociedad",
            "Athletic Club de Bilbao",
            "Deportivo Alavés",
            "Getafe CF",
            "Sevilla FC",
            "Levante UD",
            "Granada CF",
            "CA Osasuna",
            "Real Valladolid CF",
            "RCD Espanyol",
            "SD Eibar",
            "RCD Mallorca",
            "CD Leganés",
        ],
    },
   ...
```

You can also create a custom league (like UCL) by picking different teams from all the available leagues.
There is no theoretical limit to the number of teams, but try to limit the number of teams to 100 and ideally try to have an even number of teams.

To make this work you will have to edit `constants/leagues.py` and add your league in it.
Ensure that you use the correct team name. For example, 'Man Utd' will not work , you will have to use 'Manchester United' because that is how it is stored.
To see the list of all valid team names, you can execute the following command:

```bash
python simulator/scripts/all_teams.py
```

Currently simMatch() will simulate the match in its entirety and update the league table. But there are functions that can be used to see the timeline of a match as it happens. In future builds, the user will be able to take charge of a particular team and see the events of any game that he is involved in live.

## Supported Leagues

Top 5 Leagues are natively supported:

* English Premier League
* La Liga
* Seria A
* Bundesliga
* Ligue 1

## Sample Output

Following is the output of a fully simulated league:

![Screenshot (2)](https://user-images.githubusercontent.com/55048030/84644685-1b96c700-af1d-11ea-81af-6ea056cbdea5.png)

## Feedback and Support

Please feel free to play around with the code and let me know if you find any issues or you need some help with certain functions.</br>
You can contact me at <allen.thomas.dev@gmail.com>
