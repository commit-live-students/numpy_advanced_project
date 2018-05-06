# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np


def get_total_deliveries_played(batsman):
    batsman = str.encode(batsman)
    ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    deliveries = ipl_matches_array[:,13]
    batsman_deliveries = (deliveries == batsman)
    unique, counts = np.unique(batsman_deliveries, return_counts=True)
    return dict(zip(unique, counts))[True]


