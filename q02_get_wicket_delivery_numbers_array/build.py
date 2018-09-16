# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    # delievery column which has to be given in op is considered as main dataset
    delivery = ipl_matches_array[:,11]
    
    # [create filter: batsman] accesssing the column playerout 
    playerout = ipl_matches_array[:,20]==batsman
    
    #apply the filter in the main data(deliveries to get the values)
    deliveries_out=delivery[playerout].astype()
    
    return(deliveries_out)

get_wicket_delivery_numbers_array(b'ST Jayasuriya')

import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=0, delimiter=',')


def get_wicket_delivery_numbers_array(batsman):
    # delievery column which has to be given in op is considered as main dataset
    delivery = ipl_matches_array[:,11]
            
    # [create filter: batsman] accesssing the column playerout 
    playerout = ipl_matches_array[:,20]==batsman.encode()
    
    #apply the filter in the main data(deliveries to get the values)
    return delivery[playerout].astype(float)

get_wicket_delivery_numbers_array('ST Jayasuriya')
playerout = ipl_matches_array[:,20:21].astype(np.string_)==b'ST Jayasuriya'
playerout
]
delivery_out[playerout]
type(delivery_out)


