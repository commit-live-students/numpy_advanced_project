# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_toss_win_count(player):
    teams = np.array([])
    for x in ipl_matches_array:
        if x[3]==player or x[4]==player:
            team= (x[5])
            teams= np.append(teams, team)
    return len(set(teams))

#Your Solution




