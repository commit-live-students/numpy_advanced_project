# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    sum_deliveries = int((ipl_matches_array[:,[13]] == batsman).sum())
    #print(sum_deliveries)
    return sum_deliveries
#get_total_deliveries_played('SR Tendulkar')
