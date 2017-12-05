# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    delivery=0
    bats=ipl_matches_array[:,13]
    bat_del=bats[bats == batsman]
    print bat_del
    for i in bat_del:
            delivery+=1
    return delivery
