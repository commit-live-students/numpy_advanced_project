# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd

ipl_matches_array1 =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
ipl_matches_array=ipl_matches_array1.astype(np.str)
#Your Solution
def get_wicket_delivery_numbers_array(players):
    
    player_out=(ipl_matches_array[:,-3]==players)
    a=np.array(ipl_matches_array[:,11])
    return a[player_out]
    




