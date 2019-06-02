# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    deliveryPlayer = ipl_matches_array[:,[11,20]]
    deliveries = [];
    for entry in deliveryPlayer:
        if(entry[1] == player):
            deliveries.append(float(entry[0]))
    return np.array(deliveries)


