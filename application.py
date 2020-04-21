import constants
import copy
import statistics

players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)
experienced_players = []
noobs = []
panthers = []
bandits = []
warriors = []


def experience_check():
    for player in players_copy:
        if player['experience'] == 'YES':
            player['experience'] = True
            experienced_players.append(player)
        else:
            player['experience'] = False
            noobs.append(player)


def height_splitter():
    for player in players_copy:
        player['height'] = int(player['height'].split(' ')[0])


def guardian_string():
    for player in players_copy:
        player['guardians'] = player['guardians'].replace(' and', ',')


def team_builder(team1, team2, team3):
    while len(experienced_players) > 0:
        if len(team1) == (len(team2) + len(team3)) / 2:
            team1.append(experienced_players.pop())
        elif len(team1) > len(team2):
            team2.append(experienced_players.pop())
        else:
            team3.append(experienced_players.pop())

    while len(noobs) > 0:
        if len(team1) == (len(team2) + len(team3)) / 2:
            team1.append(noobs.pop())
        elif len(team1) > len(team2):
            team2.append(noobs.pop())
        else:
            team3.append(noobs.pop())

def team_height(team):
    all_heights = [player['height'] for player in team]
    return statistics.mean(all_heights)



experience_check()
height_splitter()
guardian_string()
team_builder(panthers, bandits, warriors)
print(panthers)
print(bandits)
print(warriors)
team_height(panthers)
