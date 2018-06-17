# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype=np.str, skip_header=1, delimiter=',')


def get_wicket_delivery_numbers_array(player_out):
    delivery= np.array([])
    ipl_del=ipl_matches_array[ipl_matches_array[:,20]==player_out]
    return ipl_del[:,11]

get_wicket_delivery_numbers_array('ST Jayasuriya')






