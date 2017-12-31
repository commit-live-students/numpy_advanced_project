# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution

def get_total_deliveries_played(batsman):
    val=ipl_matches_array[:,13]
    res=np.count_nonzero(val[:]==batsman)
    return res
get_total_deliveries_played('ST Tendulkar')
