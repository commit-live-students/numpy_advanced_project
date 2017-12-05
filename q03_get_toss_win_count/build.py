#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

def get_toss_win_count(Team):
    unique_matches = np.unique(ipl_matches_array[:,0:1])
    #print unique_matches
    #print ipl_matches_array[:,5]
    rows = np.where(ipl_matches_array[:,5]==Team)
    return np.unique(ipl_matches_array[rows,0][0]).shape[0]

print get_toss_win_count(Team='Mumbai Indians')
