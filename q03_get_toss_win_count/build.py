# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype=np.str, skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    ipl_toss = ipl_matches_array[ipl_matches_array[:,5] == team]
    return(len(np.unique(ipl_toss[:,0])))
          
get_toss_win_count('Mumbai Indians')    


