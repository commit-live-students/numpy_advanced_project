from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
#ipl_matches_array = np.genfromtxt("data/ipl_matches_small.csv",skip_header = 1, dtype="|S50", delimiter=",")
#Your Solution
def get_toss_win_count(teams):
    row1 = np.where(ipl_matches_array[:, 5:6] == teams)
    #row1 = list(row1)
    return np.unique(ipl_matches_array[row1, 0]).shape[0]
    #print type(row1)


print get_toss_win_count(teams = "Mumbai Indians")
