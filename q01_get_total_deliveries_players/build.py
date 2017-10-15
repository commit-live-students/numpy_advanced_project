# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv",dtype="|S50",delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    ipl_match=ipl_matches_array[:,13]
    ipl_match_d=list(ipl_match)
    count=ipl_match_d.count(batsman)
    return count

get_total_deliveries_played("SR Tendulkar")
