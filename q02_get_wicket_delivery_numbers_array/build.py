# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
#ipl_matches_array[ipl_matches_array[:,-3] == 'ST Jayasuriya']
#Your Solution
def get_wicket_delivery_numbers_array(player):
    out_deliveries = ipl_matches_array[:,11][ipl_matches_array[:,-3] == player]
    #print(type(out_deliveries))
    return out_deliveries
a =get_wicket_delivery_numbers_array('ST Jayasuriya')
print(a)


