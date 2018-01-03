# Default imports
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution

def get_total_deliveries_played(batsman):
    df_ipl_matches = DataFrame(ipl_matches_array)
    df_batsman_count = df_ipl_matches[13].value_counts()
    return int(df_batsman_count[batsman])
