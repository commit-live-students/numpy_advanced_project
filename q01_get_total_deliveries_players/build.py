# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_total_deliveries_played(batsman):
    n1=ipl_matches_array[:,-10]
    n1 = n1[n1==batsman]
    return n1.size
