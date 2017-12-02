#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
from pandas import Series as Series

def create_runs_series(match_code):
    matches = ipl_matches_array  [:,(0,11,16)]
    match= matches[ matches[:,0]==match_code]
    return Series(data=match[:,2],index=match[:,1])
