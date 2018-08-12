# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    sliced_batsman=ipl_matches_array[:,13:14]
    player_count=np.where(sliced_batsman == batsman)
    count=len(player_count[0])
    return count
