# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_total_deliveries_played(batsman):
    filter1 = ipl_matches_array[:,13] == batsman
    del_played = len(ipl_matches_array[filter1])
    return del_played
