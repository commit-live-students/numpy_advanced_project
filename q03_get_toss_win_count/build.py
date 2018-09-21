#%load q03_get_toss_win_count/build.py

import numpy as np

path='./data/ipl_matches_small.csv'

def get_toss_win_count(team):
    

    arr=np.genfromtxt(path,delimiter=',',dtype='|S20',skip_header=1 )
    arr1=(arr[:,5]==b'Mumbai Indians')
    #print(np.unique(arr[:,0:1][arr1]).size)
    cnt=np.unique(arr[:,0:1][arr1]).size
    return cnt

b'Mumbai Indians'


