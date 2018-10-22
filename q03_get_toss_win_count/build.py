# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
import pandas as pd

toss_team = b'Mumbai Indians'

def get_toss_win_count(team_name):

    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    count=0
    match_code = np.unique(ipl_matches_array[:,0])
    for i in match_code:
        if ipl_matches_array[np.argmax(ipl_matches_array[:,0]==i),5] == team_name:
            count= count + 1
    return count

get_toss_win_count(toss_team)


