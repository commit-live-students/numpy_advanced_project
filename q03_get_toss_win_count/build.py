# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    matches , index = np.unique(ipl_matches_array[:,[0]], return_index=True)
    count = 0
    for match in index:
        if ipl_matches_array[match,5] == team :
            count = count+1
    return count

