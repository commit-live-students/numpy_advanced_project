#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
from pandas import Series

def create_runs_series(match_code):
    runs = []
    indx = []
    for i in ipl_matches_array:
        if match_code == i[0]:
            indx.append(i[11])
            runs.append(i[16])
            actual = Series(runs, dtype = np.int16, index = indx)
    return actual

actual = create_runs_series('392203')
