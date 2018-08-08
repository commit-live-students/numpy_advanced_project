# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np



# Your Solution
def get_total_deliveries_played(batsman):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    
    bats,counts=np.unique(ipl_matches_array[0:,13],return_counts=True)
    
    bats_counts=dict(zip(bats,counts))
    return bats_counts[batsman]






