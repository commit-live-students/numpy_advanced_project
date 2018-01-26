#Default Imports
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code):
    df_ipl_matches = DataFrame(ipl_matches_array)
    df_filtered = df_ipl_matches[df_ipl_matches[0]==match_code]
    return df_filtered[[11,16]].set_index(11).iloc[:,0]
