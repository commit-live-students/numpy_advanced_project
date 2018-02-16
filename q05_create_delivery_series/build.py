#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_delivery_series():
    deliv_col = ipl_matches_array[:,11]
    deliv_series = pd.Series(deliv_col)
    return deliv_series
