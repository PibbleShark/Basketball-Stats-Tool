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


def guardian_list():
    for player in players_copy:
        player['guardians'] = player['guardians'].split(' and ')
        # player['guardians'] = player['guardians'].replace(' and', ',')
        # instructions said to make a list, but this code seemed a more simple way to ge the same output


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
    return round(statistics.mean(all_heights))


def display_players(team):
    player_string = ', '.join([player['name'] for player in team])
    return player_string


def roster_size(team):
    total_size = len(team)
    experienced = 0
    for player in team:
        if player['experience'] is True:
            experienced += 1
        else:
            pass
    return [total_size, experienced, (total_size - experienced)]


def team_guardians(team):
    guardian_lst = [', '.join(player['guardians']) for player in team]
    guardian_string = ', '.join([str(guardian) for guardian in guardian_lst])
    return guardian_string
    #', '.join([player['guardian'] for player in team])
    # this is the second part of the code I had originally written
    # though I do see that converting the guardians to a list could have other advantages


def teams_stats_display(team, index):
    print(f"""
    {teams_copy[index].upper()}
    {'-' * 40}
    Players: {display_players(team)}
    Total Players: {roster_size(team)[0]}
    Experienced Players: {roster_size(team)[1]}
    Players Without Experience: {roster_size(team)[2]}
    Average Height of Players: {team_height(team)} inches
    Player's Guardians: {team_guardians(team)}
    """)


def display_data():
    heading = f"""
    WELCOME TO THE BASKETBALL STATS TOOL
    {'-' * 40}
    MAIN MENU:
    """
    print(heading)
    input("Press Enter to continue")
    team_display = f"""
    {'-' * 40}
    1) {teams_copy[0]}
    2) {teams_copy[1]}
    3) {teams_copy[2]}
    4) Exit Program
    {'-' * 40}
    """
    print(team_display)

    while True:
        team_select = input("Enter the number that corresponds to the team you would like to view or enter 4 "
                            "to exit   ")

        try:
            team_select = int(team_select)
            if team_select not in range(1, 5):
                raise ValueError

        except ValueError:
            print("that answer does not correspond to one of our teams")
            continue

        if team_select == 1:
            teams_stats_display(panthers, 0)
            input("Press Enter to continue")
            print(team_display)

        elif team_select == 2:
            teams_stats_display(bandits, 1)
            input("Press Enter to continue")
            print(team_display)

        elif team_select == 3:
            teams_stats_display(warriors, 2)
            input("Press Enter to continue")
            print(team_display)

        else:
            break


if __name__ == "__main__":
    experience_check()
    height_splitter()
    guardian_list()
    team_builder(panthers, bandits, warriors)
    display_data()
