# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def create_delivery_series():
    x= pd.Series(ipl_matches_array[:,11])
    return x
#Your Solution


x= pd.Series(ipl_matches_array[:,11])
type(x)


