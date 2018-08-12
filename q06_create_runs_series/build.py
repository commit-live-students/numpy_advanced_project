#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def create_runs_series(match_code):
    subst = np.array([val for val in ipl_matches_array if val[0] == '392203'])
    runs = subst[0:,16]
    ind_deliv = subst[0:,11]
    return pd.Series(runs, index=ind_deliv)
