# %load q05_create_delivery_series/build.py
#Default Imports
import numpy as np
import pandas as pd
ipl_matches_array=np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    
#Your Solution
def create_delivery_series():
    return pd.Series(ipl_matches_array[:,11])
    

create_delivery_series()


