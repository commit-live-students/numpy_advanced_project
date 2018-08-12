# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=0, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    deliverires =  ipl_matches_array[:,13]
    unique, counts = np.unique(deliverires, return_counts=True)
    bastman_deliveries = dict(zip(unique, counts))
    no_of_delivery = bastman_deliveries[batsman]
    return no_of_delivery

get_total_deliveries_played(batsman = 'SR Tendulkar')
