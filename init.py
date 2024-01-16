import pandas as pd
import numpy as np

# Make dataframe for player info
# Columns: Name, Elo, Top, Jungle, Mid, ADC, Support, Wins, Losses, Winrate
# df = pd.DataFrame(columns=['Name', 'Elo', 'Top', 'Jungle', 'Mid', 'ADC', 'Support', 'Wins', 'Losses', 'Winrate'])
#
# # Insert example player
# df = df.append({'Name': 'Aaron', 'Elo': 1100, 'Top': 1, 'Jungle': 0, 'Mid': 1, 'ADC': 0, 'Support': 0, 'Wins': 0, 'Losses': 0, 'Winrate': 0}, ignore_index=True)
# df = df.append({'Name': 'Aditya', 'Elo': 950, 'Top': 0, 'Jungle': 0, 'Mid': 0, 'ADC': 0, 'Support': 1, 'Wins': 0, 'Losses': 0, 'Winrate': 0}, ignore_index=True)
#
# df.to_csv('players.csv', index=False)

# Make dataframe for match history
# Columns: Date, Team 1, Team 2, Winner
df = pd.DataFrame(columns=['Date', 'Team 1', 'Team 2', 'Winner'])

df = df.append({'Date': '2020-01-01', 'Team 1': 'Aaron, Aditya', 'Team 2': 'Bosco, Brian', 'Winner': 1}, ignore_index=True)

df.to_csv('match_history.csv', index=False)
