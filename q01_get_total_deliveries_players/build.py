# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
ipl = pd.read_csv('data/ipl_matches_small.csv')
# Your Solution
def get_total_deliveries_played(name):
    name = ipl.batsman.value_counts()['SR Tendulkar']
    return name


