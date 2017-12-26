# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd
from pandas import DataFrame

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
# Your Solution
def get_total_deliveries_played(batsman):
    total = 0
    for i in ipl_matches_array:
        if batsman==i[13]:
            total = total + 1
    return total


tendulkar_total = get_total_deliveries_played('SR Tendulkar')
