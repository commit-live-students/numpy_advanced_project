#Default Imports
import pandas as pd
import numpy as np
from pandas import Series
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code):
    ipl_match_code = ipl_matches_array[ipl_matches_array[0:,0]== match_code]
    return Series(ipl_match_code[0:,16],index=ipl_match_code[0:,11])
