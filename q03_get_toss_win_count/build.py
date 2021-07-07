# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_toss_win_count(team):
    match= [x[0] for x in ipl_matches_array if x[5] == team]
    toswin = set(match)
    twin=len(toswin)
    
    return twin
 

#Your Solution




