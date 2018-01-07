# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


def create_runs_series(match_code):
    code = ipl_matches_array[:,0]
    delivery = ipl_matches_array[np.where(code==match_code)][:,11]
    runs = ipl_matches_array[np.where(code==match_code)][:,-7]
    data = pd.Series(runs,index=delivery)
    return data
