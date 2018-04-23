# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_wicket_delivery_numbers_array(player='ST Jayasuriya'):
    ipl_match = pd.read_csv('data/ipl_matches_small.csv')
    name = ipl_match['player_out']=='ST Jayasuriya'
    delivery = ipl_match['delivery'][name].values.astype(np.str)
    return delivery

get_wicket_delivery_numbers_array()


