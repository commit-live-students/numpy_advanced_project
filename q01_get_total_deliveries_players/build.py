# Default imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=0, delimiter=",")
batsman = raw_input("Enter the batsman's name: ")

def get_total_deliveries_played(batsman):
    batsman_data = ipl_matches_array[:,13]
    return list(batsman_data).count(batsman)

get_total_deliveries_played(batsman)
