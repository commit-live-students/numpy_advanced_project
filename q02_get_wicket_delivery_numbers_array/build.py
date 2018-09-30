# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    over = ipl_matches_array[:,11].astype(np.unicode_)   
    btsmn = ipl_matches_array[:,20].astype(np.unicode_)
    return over[(btsmn == player)]
    
get_wicket_delivery_numbers_array('ST Jayasuriya')


