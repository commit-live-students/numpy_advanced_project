#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(matchid):
    data = ipl_matches_array
    for i in data:
        if i[0] == matchid:
            index = data[:,11]
            runs = data[:,16]
    series = pd.Series(data = runs, index= index)
    return series
#print create_runs_series('392203')
