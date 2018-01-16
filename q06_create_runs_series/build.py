#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code):
    newipl = ipl_matches_array[np.where(ipl_matches_array[:,0]==match_code)]
    runs = newipl[:,16]
    delivery = newipl[:,11]
    data = pd.Series(runs, index=delivery)
    return data
