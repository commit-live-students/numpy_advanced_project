# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv",skip_header=1, dtype="|S50",  delimiter=",")

def get_total_deliveries_played(batsman):
    bat,count = np.unique(ipl_matches_array[:,13],return_counts=True)
    a = dict(zip(bat,count))
    return a[batsman]
