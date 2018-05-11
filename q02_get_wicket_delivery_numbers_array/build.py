# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd

def get_wicket_delivery_numbers_array(player):
    ipl_matches_array =pd.read_csv('data/ipl_matches_small.csv',index_col='match_code')
    a=ipl_matches_array['player_out']==player
    variable=ipl_matches_array[a]['delivery']
    return variable.values
#Your Solution


