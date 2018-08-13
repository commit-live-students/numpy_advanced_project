#Default Imports
import pandas as pd
from pandas import Series
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code):

    a = ipl_matches_array[:,11][[ipl_matches_array[:,0] == match_code]]
    b = ipl_matches_array[:,16][[ipl_matches_array[:,0] == match_code]]
    s  = Series(b,index = a)
    return s

print create_runs_series('392203')
