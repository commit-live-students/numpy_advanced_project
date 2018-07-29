# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
def get_wicket_delivery_numbers_array(player):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    c = ipl_matches_array[ipl_matches_array[:,-3] == player]
    deliveries = c[:,-12]
    return deliveries
#Your Solution

get_wicket_delivery_numbers_array(b'ST Jayasuriya')




