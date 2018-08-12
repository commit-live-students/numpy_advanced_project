#Default Imports
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution

def get_toss_win_count(team):
    df_ipl_matches = DataFrame(ipl_matches_array)
    df_toss = df_ipl_matches[[0,5]].drop_duplicates(subset=0)
    return df_toss[5].value_counts()[team]
