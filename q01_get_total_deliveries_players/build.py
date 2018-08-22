# %load q01_get_total_deliveries_players/build
# Default imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
path = ipl_matches_array
# Your Solution
def get_total_deliveries_played(path):
    count = 0
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    batsman = ipl_matches_array[:,-10].astype(np.str)
    batsman_series = pd.Series(batsman)
    
    for l in batsman_series:
        if l == 'SR Tendulkar':
            count+=1
    print(count)
    return count
get_total_deliveries_played(path)



