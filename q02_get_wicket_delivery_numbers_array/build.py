# %load q01_get_total_deliveries_players/build.py
import numpy as np
import pandas as pd
path = 'data/ipl_matches_small.csv'
data = pd.read_csv(path)
def get_wicket_delivery_numbers_array(batsman):
    a = data['delivery'][data['player_out']==batsman]
    list1 = np.array(a,dtype='|S4')
    return list1
