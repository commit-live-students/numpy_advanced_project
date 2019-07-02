# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    team1 = ipl_matches_array[ipl_matches_array[0:,20] == player]
    list_1 = team1[0:,11]
    return list_1







