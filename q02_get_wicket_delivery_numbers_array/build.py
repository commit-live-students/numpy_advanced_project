# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    ipl = ipl_matches_array[:,[11,20]]
    wicket_delivery=[]
    for delivery in ipl:
        if delivery[1] == player:
            wicket_delivery.append(delivery[0])
    return np.array(wicket_delivery)
get_wicket_delivery_numbers_array(b'ST Jayasuriya')

