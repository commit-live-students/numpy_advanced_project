# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
#ipl=pd.read_csv('data/ipl_matches_small.csv')
df = pd.read_csv('data/ipl_matches_small.csv')
def create_delivery_series():
    my_array = ipl_matches_array[:, 11]
    
    return pd.Series(my_array)

create_delivery_series()




