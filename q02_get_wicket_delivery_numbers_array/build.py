# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    delivery = []
    for data in ipl_matches_array:
    
        if data[20] == batsman :
            delivery.append(data[11])
    return np.array(delivery)
get_wicket_delivery_numbers_array(b'ST')



