# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
df = pd.read_csv('data/ipl_matches_small.csv')
def create_delivery_series():
    my_array = ipl_matches_array[:, 11]
    
    return pd.Series(my_array)
#ipl_matches_array[:, 11]
#ipl_matches_array[0]
#ipl_matches_array[:, 11]
type(pd.Series(ipl_matches_array[:, 11]))


