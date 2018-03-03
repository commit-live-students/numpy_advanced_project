#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def create_runs_series(match_code):
    match_code_filter = ipl_matches_array[:,0] == match_code
    match_list = ipl_matches_array[match_code_filter]
    return pd.Series(match_list[:,16],index=match_list[:,11])
#print create_runs_series('392203')
