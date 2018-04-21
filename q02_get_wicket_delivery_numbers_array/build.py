# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    c = ipl_matches_array[:,-3].astype(str) == player
    return ipl_matches_array[c][:,11].astype(str)

deliveries = get_wicket_delivery_numbers_array('ST Jayasuriya')



