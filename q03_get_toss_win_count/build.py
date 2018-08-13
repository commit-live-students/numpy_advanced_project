#Default Imports
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team='Mumbai Indians'):
    data_03 = ipl_matches_array[:,[0,5]]
    df = pd.DataFrame(data_03, columns=['match_code', 'toss_winner'])
    #pdf = df.set_index('')
    team_match = df.loc[df['toss_winner'] == team, 'match_code']
    unique_match = team_match.unique()
    final = len(unique_match)
    #match_count = df.groupby('match_code')
    #l = df.loc[df['Player_Out'] == player_Out, 'Deliveries']

    return final
print get_toss_win_count('Mumbai Indians')
