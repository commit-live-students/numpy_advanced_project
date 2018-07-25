# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
batsman = 'ST Jayasuriya'
#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    df = pd.read_csv('data/ipl_matches_small.csv')
    wicket_delivery_numbers_array = df.loc[df['player_out']==batsman]
    return wicket_delivery_numbers_array['delivery'].values


