# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(name):
    y=(ipl_matches_array)[:,13]
    s=0
    for x in y:
        if x==name:
            s+=1
    return s
    







