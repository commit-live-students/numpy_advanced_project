import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_toss_win_count(team):
    arr = ipl_matches_array[ipl_matches_array[:,5].astype('|S50') == team]
    arr1 = np.unique(arr[:,0])
    
    tosses_won = np.size(arr1)
    
    return tosses_won
    






