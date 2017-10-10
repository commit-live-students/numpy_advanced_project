# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def get_wicket_delivery_numbers_array(player):
    batsmanFilter=ipl_matches_array[:,13]==player
    outFilter=ipl_matches_array[:,20]==player
    filterArray=ipl_matches_array[batsmanFilter & outFilter]
    finalOutput=filterArray[:,11]
    return finalOutput
