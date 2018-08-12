#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code):
    arr = ipl_matches_array[ipl_matches_array[:,0]==match_code]
    return pd.Series(data=arr[:,-7], index=arr[:,-12])
