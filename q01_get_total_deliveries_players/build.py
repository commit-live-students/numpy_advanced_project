# Default imports
import numpy as np
from collections import Counter

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    col = ipl_matches_array[:,13]
    c = Counter([i for i in col])
    count = c[batsman]
    return count
