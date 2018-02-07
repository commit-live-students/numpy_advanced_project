# Default imports

import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_total_deliveries_played(batsman):
    bats_col = ipl_matches_array[:,13]
    unq = np.unique(bats_col,return_counts = True)
    plr = np.where(unq[0] == batsman)

    deliv = int(unq[1][plr])

    return deliv

print get_total_deliveries_played('SR Tendulkar')
