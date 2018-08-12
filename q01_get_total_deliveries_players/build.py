# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    cbatsman = np.unique(ipl_matches_array[:,13], return_counts=True)
    ind = np.where(cbatsman[0]==batsman)
    ans = int(cbatsman[1][ind])
    return ans
