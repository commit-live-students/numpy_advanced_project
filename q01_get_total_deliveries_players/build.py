# Default imports
import numpy as np
import pandas as pd

def get_total_deliveries_played(name):
    ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
    deliveries = ipl_matches_array[0:,11]
    batsman = ipl_matches_array[0:,13]

    del_bat = pd.Series(data = batsman, index = deliveries)
    counts = del_bat.value_counts()
    return counts[name]


# Your Solution
