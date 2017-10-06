import numpy as np
import pandas as pd
def get_total_deliveries_played(batsman):
    ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
    from collections import Counter
    x=Counter(ipl_matches_array[:,13])
    return x[batsman]


# Your Solu
