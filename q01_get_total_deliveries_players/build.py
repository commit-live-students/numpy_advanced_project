# Default imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")



batsman = 'ST Jayasuriya'
def get_total_deliveries_played(batsman):
    batsman1 = ipl_matches_array[: , 13]
    a = batsman1 == batsman
    total_deliveries = len(ipl_matches_array[a])
    return total_deliveries

get_total_deliveries_played(batsman)
# Your Solution
