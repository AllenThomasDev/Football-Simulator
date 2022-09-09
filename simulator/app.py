from simulator.leagues import League


def get_league_input():
    try:
        num = int(input('1 - La Liga Santander\n'
                        '2 - Premier League\n'
                        '3 - Bundesliga\n'
                        '4 - Seria A\n'
                        '5 - Ligue 1\n'
                        '-> '))
        assert num in [1, 2, 3, 4, 5]
        return num
    except (ValueError, AssertionError):
        print('Please enter a valid input!')
        get_league_input()


def run():
    print('Welcome to the Football League Simulator\n'
          'You can use this project to simulate Football Leagues across the world\n'
          'Please select a league that you would like to simulate: ')
    league_no = get_league_input()
    league = League(league_no)
    league.simulate_league()
