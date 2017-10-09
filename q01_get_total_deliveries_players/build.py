# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
batsman_delivery=ipl_matches_array[:,13]
def get_total_deliveries_played(batsman):
    delivery=0
    for x in batsman_delivery:
        if(x==batsman):
            delivery+=1
    return delivery

get_total_deliveries_played('SR Tendulkar')
