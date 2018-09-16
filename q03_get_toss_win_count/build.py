# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=0, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    
    #Boolean indexing to store toss wins for MI.
    MI_TossWin = ipl_matches_array[:,5]==team
    
    #getting unique toss wins based on match id as the value gets repeated per delivery.
    unique_win_count = np.unique(ipl_matches_array[MI_TossWin,0])
    
    #returning the count.
    return np.count_nonzero(unique_win_count)
    
get_toss_win_count(b'Mumbai Indians')





