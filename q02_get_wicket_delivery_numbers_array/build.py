# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    deliveries = ipl_matches_array[:, (0,11,13,20) ] #matchcode,delivery number, batsman, batsman out
    filtered_indices = np.where(deliveries[:,3] == player)
    wicket_deliveries = deliveries[filtered_indices]
    return  wicket_deliveries [:,1]






