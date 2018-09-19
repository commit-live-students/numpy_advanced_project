# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_toss_win_count(team = b'Mumbai Indians'):
        a = ipl_matches_array[ipl_matches_array[:,7] == team]
        var1 = len(np.unique(a[:,0]))
        return var1
        
    
    






