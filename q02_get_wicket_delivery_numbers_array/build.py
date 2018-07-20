# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    array1 = (ipl_matches_array[:,20] == player)
    wicket = ipl_matches_array[array1]
    return wicket[:,11]
print(get_wicket_delivery_numbers_array(b'ST Jayasuriya'))


