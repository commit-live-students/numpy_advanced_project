# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np


#Your Solution
def get_toss_win_count(team=''):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    toss= ipl_matches_array[:,0:6:5]
    teams= np.unique(toss,axis=0)
    wins= teams[teams[:,1].astype(np.str)==team]
    return wins[:,1].size
    
get_toss_win_count('Mumbai Indians')

