from leagues import League

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

n = 0
print(welcome_message)
while n not in ["1", "2", "3", "4", "5"]:
    print(leagues_message)
    n = input()
    if n not in ["1", "2", "3", "4", "5"]:
        print("Enter a Valid input")

league = League(int(n))
league.simLeague()
