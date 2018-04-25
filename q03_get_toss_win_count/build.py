# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')



#Your Solution
def get_toss_win_count(team):
    
    count = 0
   
    for a in np.unique(ipl_matches_array[:,(0,5)], axis = 0):
        b = a.astype(str)
        if(b[1] == team):
            count = count + 1
            
    return count
            
            
    
    
get_toss_win_count('Deccan Chargers')





