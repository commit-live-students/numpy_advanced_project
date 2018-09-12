# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_toss_win_count(team = b'Mumbai Indians' ):
        var1 = np.count_nonzero(ipl_matches_array[:,5] == team)
        return var1
    
    





