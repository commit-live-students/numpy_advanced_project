# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def get_total_deliveries_played(player):
    occ_player = np.where(ipl_matches_array[0:,13] == 'SR Tendulkar',1,0)
    get_total_deliveries = np.sum(occ_player)
    return get_total_deliveries

# Your Solution
