# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    count = 0 
    toss_win_team = np.stack(ipl_matches_array[:,[0,5]])
    zip_team = np.unique(toss_win_team, axis=0)
    for k in list(zip_team[:,1]):
        if (k == team):
            count+=1
            
    return (count)

get_toss_win_count(b'Mumbai Indians')


