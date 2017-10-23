# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    l = [i[0] for i in ipl_matches_array  if i[13] == batsman]
    return len(l)
