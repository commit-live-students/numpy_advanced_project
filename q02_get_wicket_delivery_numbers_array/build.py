# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player_out):
    delivery=ipl_matches_array[:,(11)]
    pl_out=(ipl_matches_array[:,(20)]==player_out)
    print(type(ipl_matches_array[21,20]),ipl_matches_array[21,20])
    print(delivery[pl_out])
    return(delivery[pl_out])


get_wicket_delivery_numbers_array(b'ST Jayasuriya')



