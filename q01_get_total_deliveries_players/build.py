# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    all_batsman_deliveries = ipl_matches_array[:,[11,13]]
    batsman_deliveries = all_batsman_deliveries[all_batsman_deliveries[:,1] == batsman][:,0]
    number_deliveries = batsman_deliveries.shape[0]

    return number_deliveries

get_total_deliveries_played('SR Tendulkar')
