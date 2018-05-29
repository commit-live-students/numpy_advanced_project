# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array1 =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
ipl_matches_array = ipl_matches_array1.astype(np.str)

#Your Solution
def get_toss_win_count(team):
    
    match_code=(np.unique(ipl_matches_array[:,0]))
    match_team=(ipl_matches_array[:,7]==team)
    return (len(np.intersect1d(ipl_matches_array[match_team][:,0],match_code)))



