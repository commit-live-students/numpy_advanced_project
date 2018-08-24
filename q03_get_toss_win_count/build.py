# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
path = ipl_matches_array
team = 'Mumbai Indians'
#Your Solution
def get_toss_win_count(team):
    team_records = path[path[:, 5] == team]
    unique_match = set(team_records[:, 0])
    print (len(unique_match))
    return len(unique_match)
get_toss_win_count(team)
        




