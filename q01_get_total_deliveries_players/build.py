# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_wicket_delivery_numbers_array(player):
    wick_deliveries = []
    rows = ipl_matches_array.shape[0]
    
    for i in range(0,rows):
        if ipl_matches_array[i][20] == player:
            wick_deliveries.append(ipl_matches_array[i][11])
    return np.array(wick_deliveries)





