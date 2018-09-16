# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    
    unique, counts = np.unique(ipl_matches_array[:,5], return_counts=True)
    d=dict(zip(unique, counts))
    
    toss=d['Mumbai Indians']
    
    return toss
    




