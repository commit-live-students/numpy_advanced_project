# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_toss_win_count(team):
    a,i=np.unique(ipl_matches_array[:,0],return_index=True)
    n,j=np.unique(ipl_matches_array[i,5],return_counts=True)
    d=dict(zip(n,j))
    return (d[team])
get_toss_win_count(b'Mumbai Indians')



