# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    Toss_win=ipl_matches_array[:,5]==team
    
    unique_win_count = np.unique(ipl_matches_array[Toss_win,0])
    
    return np.count_nonzero(unique_win_count) #returning the count.
    
get_toss_win_count(b'Mumbai Indians')
    
    





