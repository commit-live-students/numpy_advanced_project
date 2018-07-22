# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution

def get_wicket_delivery_numbers_array(player_out):
    '''Function to return deliveries of player when out'''
    deliveries = (ipl_matches_array[ipl_matches_array[:,-3]==player_out])[:,-12]
    return deliveries

#call the function to get the arrays
get_wicket_delivery_numbers_array(b'ST Jayasuriya')



