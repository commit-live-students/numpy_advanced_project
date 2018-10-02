# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
#Your Solution
def get_toss_win_count(team):
    
    t = ipl_matches_array[:,5] == team

    return len(set(ipl_matches_array[t][:,1]))

get_toss_win_count('Mumbai Indians')



