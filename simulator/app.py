from simulator.league import League

welcome_message = """
Welcome to the League Simulator!
You can use this project to simulate Football Leagues across the world
Please enter the league you would like to simulate:
"""

leagues_message = """
1 - La Liga Santander
2 - Premier League
3 - Bundesliga
4 - Seria A
5 - Ligue 1
"""

def get_league_input():
    try:
        num = int(input(leagues_message))
        assert num in [1, 2, 3, 4, 5]
        return num
    except (ValueError, AssertionError):
        print('Please enter a valid input!')
        get_league_input()


def run():
    print(welcome_message)
    league_no = get_league_input()
    league = League(league_no)
    league.simLeague()
