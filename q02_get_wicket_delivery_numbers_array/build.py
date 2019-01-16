# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution


#Your Solution
def get_wicket_delivery_numbers_array(player):
    wicket_filter = (ipl_matches_array[:, 20] == player)
    wickets_arr = ipl_matches_array[wicket_filter]
    return wickets_arr[:, 11]
get_wicket_delivery_numbers_array('ST Jayasuriya')



