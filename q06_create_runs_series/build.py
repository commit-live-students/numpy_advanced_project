#Default Imports
from pandas import Series
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
match_code='392203'
def create_runs_series(match_code):
    match_code_data=ipl_matches_array[np.where(ipl_matches_array[:,0]==match_code)]
    delivery_index=match_code_data[:,11]
    run_series=Series(match_code_data[:,17],index=delivery_index)
    return run_series
