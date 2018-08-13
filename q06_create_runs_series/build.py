#Default Imports
import pandas as pd
import numpy as np

def create_runs_series(match_code):
    ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header = 1, delimiter=",")
    match_code_array = ipl_matches_array[np.where(ipl_matches_array[0:,0] == match_code)]
    runs=match_code_array[0:,16]
    delivery=match_code_array[0:,11]
    s=pd.Series(data=runs,index=delivery)
    return s


#Your Solution
