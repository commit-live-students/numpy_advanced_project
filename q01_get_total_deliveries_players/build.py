# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_total_deliveries_played(batsman):
    ipl_match = ipl_matches_array[:,13]
    ipl_match_list = list(ipl_match)
    count_deliveries= ipl_match_list.count("SR Tendulkar")
    return count_deliveries
