#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def create_delivery_series():
    deliv_series = pd.Series(ipl_matches_array[0:,11])
    return deliv_series
#Your Solution
