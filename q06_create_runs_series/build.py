#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def create_runs_series(match_code):
    matches=ipl_matches_array[np.where (ipl_matches_array[:,0]==match_code)]
    runs=pd.Series(matches[:,16],index=matches[:,11])
    return runs
