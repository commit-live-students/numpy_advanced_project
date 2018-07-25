# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
batsman = 'SR Tendulkar'
# Your Solution

def get_total_deliveries_played(batsman):
    df = pd.read_csv('data/ipl_matches_small.csv')
    df1 =df.loc[df['batsman']==batsman]
    total_deliveries_played = df1['batsman'].count().astype(np.int32)
    return total_deliveries_played


