#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution

def create_delivery_series():
    #print(ipl_matches_array[0])
    return pd.Series(ipl_matches_array[:,11])

#print(create_delivery_series())
