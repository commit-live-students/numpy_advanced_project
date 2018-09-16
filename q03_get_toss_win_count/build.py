# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team='Mumbai Indians'):
    
    arr=ipl_matches_array[:,[0,5]]
    arr1=np.unique(arr,axis=0)
    
    unique,counts=np.unique(arr1[:,1],return_counts=True)
    d=dict(zip(unique,counts))
    
    toss=d[team]
    
    return toss
    




