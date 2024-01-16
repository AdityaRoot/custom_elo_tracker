# Credits to Bosco Li for the original maths on excel
import numpy as np
import pandas as pd

players = pd.read_csv('players.csv')
matches = pd.read_csv('match_history.csv')



def insert_player():
    # Insert player into database
    print(f'Current Database \n\n {players}')
    name = input("Player Name: ")
    elo = int(input("Player Elo: "))

    if name in players['Name'].values:
        print("Player already exists")
        return
    
    role = input("Player Roles [tjmas]: ")
    for i in role:
        if i not in ['t','j','m','a','s']:
            print("Invalid Role")
            return

    new_players = players.append({'Name': name, 'Elo':elo, 'Top': 1 if 't' in role else 0, 'Jungle': 1 if 'j' in role else 0, 'Mid': 1 if 'm' in role else 0, 'ADC': 1 if 'a' in role else 0, 'Support': 1 if 's' in role else 0, 'Wins': 0, 'Losses':0, 'Winrate':0}, ignore_index=True)
    print(new_players)
    if input('Save? [y/n]') == 'y':
        new_players.to_csv('players.csv', index=False)

    print(role)

def modify_player():
    # Modify player in database
    print(f'Current Database \n\n {players}')
    name = input("Player Name: ")
    if name not in players['Name'].values:
        print("Player does not exist")
        return
    new_name = input("Player Name: ")
    elo = int(input("Player Elo: "))
    role = input("Player Roles [tjmas]: ")
    for i in role:
        if i not in ['t','j','m','a','s']:
            print("Invalid Role")
            return
    players.loc[players['Name'] == name, 'Name'] = new_name
    players.loc[players['Name'] == name, 'Elo'] = elo
    players.loc[players['Name'] == name, 'Top'] = 1 if 't' in role else 0
    players.loc[players['Name'] == name, 'Jungle'] = 1 if 'j' in role else 0
    players.loc[players['Name'] == name, 'Mid'] = 1 if 'm' in role else 0
    players.loc[players['Name'] == name, 'ADC'] = 1 if 'a' in role else 0
    players.loc[players['Name'] == name, 'Support'] = 1 if 's' in role else 0
    print(players)
    if input('Save? [y/n]') == 'y':
        players.to_csv('players.csv', index=False)

def custom_lobby(lobby):
    for i in lobby:
        print(f'{lobby.index(i)}: {i}')
    team = input("Team 1: Input numbers (no seperator): ")
    team_1 = []
    for i in team:
        team_1.append(lobby[int(i)])

    team_2 = []
    for i in range(len(lobby)):
        if lobby[i] not in team_1:
            team_2.append(lobby[i])
    print('Team 1:\n ', team_1)
    print('Team 2:\n ', team_2)


def create_lobby():
    # print(f'Current Database \n\n {players}')
    lobby = []
    while len(lobby) < 10:
        name = input(f"Player Name: ")
        if name not in players['Name'].values:
            print("Player does not exist")
            continue
        if name in lobby:
            print("Player already in lobby")
            continue
        lobby.append(name)

    while True:
        print('Lobby:\n ', lobby)
        print('1. Custom Teams')
        print('2. Matched Teams')
        print('3. Swap Players')
        print('q. Return to Main Menu')
        selection = input("What do: ")
        if selection == '1':
            custom_lobby(lobby)
            break
        elif selection == '2':
            pass
            # matched_lobby()
            # break
        elif selection == '3':
            print('Lobby:\n ', lobby)
            player_1 = input("Player to replace: ")
            if player_1 not in lobby:
                print("Player not in lobby")
                continue
            player_2 = input("Player to replace with: ")
            if player_2 not in players['Name'].values:
                print("Player does not exist")
                continue
            if player_2 in lobby:
                print("Player already in lobby")
                continue
            lobby[lobby.index(player_1)] = player_2
        elif selection == 'q':
            break




while __name__ == "__main__":
    print('1. Insert Player')
    print('2. Modify Player')
    print('3. Create Lobby')
    # print('4. Custom Teams\n')
    # print('5. Matched Teams\n')
    
    print('d. Debug')
    print('q. Quit')
    selection = input("What do: ")
    if selection == '1':
        insert_player()
        players = pd.read_csv('players.csv')

    if selection == '2':
        modify_player()

    if selection == '3':
        create_lobby()


    if selection == 'd':
        print(players)
    if selection == 'q':
        break
