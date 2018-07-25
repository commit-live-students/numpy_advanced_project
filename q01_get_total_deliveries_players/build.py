# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
from collections import Counter

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman):
    a = Counter(ipl_matches_array[:,-10])
    return a[batsman]


