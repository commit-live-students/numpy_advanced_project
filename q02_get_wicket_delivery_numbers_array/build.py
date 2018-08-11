# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    
    arr = []
    for i in range(len(ipl_matches_array)):
        if ipl_matches_array[i][20] == player:
            arr.append(ipl_matches_array[i][11])
    return arr
get_wicket_delivery_numbers_array(b'ST Jayasuriya')


