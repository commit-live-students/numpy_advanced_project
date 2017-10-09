# %load q06_create_runs_series/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np

#Your Solution

def create_runs_series(match_code):
    match_code_filter=ipl_matches_array[:,0]==match_code
    #print(match_code)
    filter_match_data=ipl_matches_array[match_code_filter]
    pIndex_delivery =filter_match_data[:,11]
    pValues_run=filter_match_data[:,16]
    match_del_run_series=pd.Series(pValues_run,pIndex_delivery)
    return match_del_run_series
