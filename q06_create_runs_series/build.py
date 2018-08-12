#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=0, delimiter=",")

def create_runs_series(match_code):
    d1 = pd.DataFrame(ipl_matches_array, columns=ipl_matches_array[0] )
    d2 = d1.set_index('delivery')
    runs = d2.iloc[:,15][d2.iloc[:, 0] == '392203']
    return runs

create_runs_series('392203')
