#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution

def create_runs_series(match_code):
    delivery = []
    runs = []

    for i in ipl_matches_array[:,[0,11,18]]:
        if i[0] == match_code:
            runs.append(i[2])
            delivery.append(i[1])

    return pd.Series(runs,delivery)
