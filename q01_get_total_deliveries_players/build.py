# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman):
    batsmen = ipl_matches_array[:,13].astype(str)
    played_by_batsman = [b == batsman for b in batsmen]
    deliveries = sum(played_by_batsman)
    return deliveries

get_total_deliveries_played('SR Tendulkar')


