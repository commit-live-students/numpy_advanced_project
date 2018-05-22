# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd


#Your Solution
def get_wicket_delivery_numbers_array(player):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv',dtype='|S50', skip_header=1, delimiter=',')
    deliveries = ipl_matches_array[:,11]
    condn = ipl_matches_array[:,20].astype(str) == str(player)
    result = deliveries[condn].astype(str)
    
    return np.array(result)

get_wicket_delivery_numbers_array('ST Jayasuriya')

