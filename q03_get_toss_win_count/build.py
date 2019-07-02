# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_toss_win_count(team):
    team_data = ipl_matches_array[ipl_matches_array[0:,5] == team]   
    tosses_won = len(list(set(team_data[0:,0])))
    return tosses_won




