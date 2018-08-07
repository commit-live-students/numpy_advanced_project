# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    deliveries = []
    delivery_wicket_details = ipl_matches_array[:, (11, 20)]
    for delivery_wicket in delivery_wicket_details:
        if (delivery_wicket[1] == player):
            deliveries.append(delivery_wicket[0])
    
    return deliveries
get_wicket_delivery_numbers_array(b'ST Jayasuriya')


