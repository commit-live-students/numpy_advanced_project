# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd

ipl_matches_array =pd.read_csv('data/ipl_matches_small.csv')

def get_wicket_delivery_numbers_array(player):
    deliveries = np.array(ipl_matches_array[ipl_matches_array['player_out'] == player]['delivery'])
    return deliveries
#Your Solution

get_wicket_delivery_numbers_array('ST Jayasuriya')


