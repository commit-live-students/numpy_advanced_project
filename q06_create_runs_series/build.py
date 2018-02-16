#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code):
    deliv_col =ipl_matches_array[:,11][ipl_matches_array[:,0]==match_code]
    run_scored =ipl_matches_array[:,16][ipl_matches_array[:,0]==match_code]
    return pd.Series(run_scored,index=deliv_col)
