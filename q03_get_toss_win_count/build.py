# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
ipl_match = pd.read_csv('data/ipl_matches_small.csv')

#Your Solution
def get_toss_win_count(team='Mumbai Indians'):

    toss_winner = ipl_match['toss_winner']==team
    unique_matches = ipl_match['match_code'][toss_winner].unique()
    count = len(unique_matches)
    return count

get_toss_win_count(team='Deccan chargers')

