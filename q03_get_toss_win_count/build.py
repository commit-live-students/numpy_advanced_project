# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    arr = np.unique(ipl_matches_array[:,[0,5]], axis=0)
    return arr[np.where(arr[:,1:] ==team )].size


arr = np.unique(ipl_matches_array[:,[0,5]], axis=0)
arr = arr[np.where(arr[:,1:] ==b'Mumbai Indians' )]
arr.size


