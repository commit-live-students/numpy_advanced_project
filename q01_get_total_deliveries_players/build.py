# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    batsman_array = ipl_matches_array[:, 13]
    batsman_filter = batsman_array == batsman
    total_deliveries = len(ipl_matches_array[batsman_filter])
    return total_deliveries
