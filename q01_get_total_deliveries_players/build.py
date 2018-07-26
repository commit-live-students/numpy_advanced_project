# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_total_deliveries_played(batsman):
    unique, counts = np.unique(ipl_matches_array[:,13],return_counts=True)
    batsman_count = dict(zip(unique, counts))
    return int(batsman_count[batsman])

get_total_deliveries_played(b'SR Tendulkar')



