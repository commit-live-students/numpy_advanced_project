#Default Imports
import pandas as pd
from pandas import Series
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code):
    i_match_code_col_index = 0
    i_delivery_col_index = 11
    i_runs_col_index = 16

    np_arr_match = ipl_matches_array[ipl_matches_array[:,i_match_code_col_index] == match_code]

    runs_arr = np_arr_match[:,i_runs_col_index]
    delivery_arr = np_arr_match[:,i_delivery_col_index]
    s_delivery_runs = Series(data=runs_arr,index=delivery_arr)
    return s_delivery_runs
