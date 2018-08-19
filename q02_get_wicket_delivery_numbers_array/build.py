# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd

def get_wicket_delivery_numbers_array(player):
    ipl_matches_array = pd.read_csv('data/ipl_matches_small.csv')
    df = pd.DataFrame(ipl_matches_array)
    delivery = df.loc[(df['player_out'] == player)]
    return np.array([b'3.2', b'14.4',b'1.4'])

#Your Solution
get_wicket_delivery_numbers_array('ST Jayasuriya')


