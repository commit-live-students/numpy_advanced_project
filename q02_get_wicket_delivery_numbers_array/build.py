# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=0, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    
    # We'll make use of boolean indexing to fetch the desired result.
    # batsman_out would store all the row values which have to be fetched.
    batsman_out = ipl_matches_array[:,-3]==player.encode()
    
    #As we have to fetch the delivery, we put 11 in the coulmn and batsman_out in row.
    return ipl_matches_array[batsman_out,11].astype(float)


#Call to the function - 
get_wicket_delivery_numbers_array('SR Tendulkar')






