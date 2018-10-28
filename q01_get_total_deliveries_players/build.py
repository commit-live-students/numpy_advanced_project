#%load q01_get_total_deliveries_players/build.py

import numpy as np

path='./data/ipl_matches_small.csv'

def get_total_deliveries_played(batsman) :
    
#ST Jayasuriya
    arr=np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)
    arr1=arr[:,13]
    
    #arr2=np.count_nonzero(ar1=='bt')
    #arr3=[arr1==bt]
    
    return np.count_nonzero(arr1==batsman)

    #print(arr1==bt)
    
get_total_deliveries_played(b'SR Tendulkar')



