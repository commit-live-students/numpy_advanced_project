# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman = 'ST Jayasuriya'):
    a = ipl_matches_array[0:,13]
#     b = batsman.values('ST Jayasuriya')
#     b = ipl_matches_array[batsman]
    b = (a == batsman)
    c = a[b]
    d = len(c)
    return d
