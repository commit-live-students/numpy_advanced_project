# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
 
team=ipl_matches_array[:,5]

def get_toss_win_count(team):
    team_bool=ipl_matches_array[:,5]==team
    arr=ipl_matches_array[:,0][team_bool]
    total_toss=np.unique(arr)
    return np.count_nonzero(total_toss)

    #uniques,counts=np.unique(winner,return_counts=True)
    #print(uniques)
    #print(counts)
    


get_toss_win_count(team)


