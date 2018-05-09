# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype=str, skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team= 'Mumbai Indians'):
    team_records = ipl_matches_array[ipl_matches_array[:, 5] == team]
    unique_matches = set(team_records[:, 0])
    print(unique_matches)
    return len(unique_matches)
get_toss_win_count()

