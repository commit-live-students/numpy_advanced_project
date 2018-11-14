# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution

def get_wicket_delivery_numbers_array(player):
    out_deliveries = ipl_matches_array[:,11][ipl_matches_array[:,-3] == player]
    return out_deliveries
x = get_wicket_delivery_numbers_array('Sachin Tendulkar')
print(x)


