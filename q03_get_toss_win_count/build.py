# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    teams = ipl_matches_array[:,[0,5]]
    winner = []
    for x in teams:
           if x[1]==team:
                winner.append(x[0])
    return int(len(set(winner)))
get_toss_win_count(b'Mumbai Indians')


