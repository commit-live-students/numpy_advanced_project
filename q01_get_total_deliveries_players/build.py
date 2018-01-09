# Default imports
import numpy as np

ipl_matches_array = np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def get_total_deliveries_played(player):
    return np.sum(np.where(ipl_matches_array[0:,13]==player,1,0))# Your Solution
