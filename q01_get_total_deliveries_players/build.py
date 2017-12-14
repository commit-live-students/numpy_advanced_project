# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    arr = [x[0] for x in ipl_matches_array[:, 13:14] if x[0] == batsman]
    return np.array(arr).size
