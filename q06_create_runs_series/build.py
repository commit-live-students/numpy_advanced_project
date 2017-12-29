#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code):
    ipl = ipl_matches_array[:,0]
    ipl_delivery_ind = ipl_matches_array[ipl.astype(np.int64) == 392203 ]
    runs_series = pd.Series(data = ipl_delivery_ind[:,16], index = ipl_delivery_ind[:,11] )
    return runs_series
#print create_runs_series(392203)
