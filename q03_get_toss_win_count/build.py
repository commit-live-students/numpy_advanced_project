# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_toss_win_count(team):
    a=ipl_matches_array[ipl_matches_array[:,5].astype(str)==team]
    b=np.unique(a[:,0])
    return len(b)
get_toss_win_count('Mumbai Indians')



