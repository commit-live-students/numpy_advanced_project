# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_total_deliveries_played(batsman):

    batsman_array = ipl_matches_array[:,13]
    unique, counts = np.unique(batsman_array, return_counts=True)
    batsman_list = zip(unique,counts)

    for ele in batsman_list:
        if ele[0] == batsman:
            return ele[1]
