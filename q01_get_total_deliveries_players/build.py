# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_total_deliveries_played(batsman):
   
    
    '''while len(batsman):
        if batsman[count] == 'SR Tendulkar':
            count+=1'''
    deliveries = 0    
    for ima in ipl_matches_array:
        if ima[13] == batsman:
            deliveries +=1
                   
    return deliveries








