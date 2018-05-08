# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_total_deliveries_played(batsman):
    
    ipl_df=pd.read_csv('data/ipl_matches_small.csv')
    return ipl_df['batsman'][ipl_df['batsman']==batsman].count()
    
    
# Your Solution




