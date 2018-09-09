import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype= '|S50', skip_header=1, delimiter=',')


def get_total_deliveries_played(batsman):
    arr = ipl_matches_array[ipl_matches_array[:,13].astype('|S50') == batsman]
    deliveries = len(arr[:,11])
    
    return deliveries
    

    



