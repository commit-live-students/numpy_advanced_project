#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code):
    match_code_data = ipl_matches_array[np.where(ipl_matches_array[:,0] == match_code)]
    #print type(match_code_data)
    #print match_code_data
    runs = pd.Series(match_code_data[:, 16], index=match_code_data[:,11])
    #print type(runs)
    return runs

create_runs_series('335987')
