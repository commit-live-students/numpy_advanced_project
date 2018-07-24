# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
team=b'Mumbai Indians'

def get_toss_win_count(team):
    match_toss_array=ipl_matches_array[:,[0,5]]
    team_filter=match_toss_array[:,1]==team
    
    toss_win=np.unique(match_toss_array[team_filter][:,[0]]).size
    
    return toss_win

get_toss_win_count(team)


