# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
data_df = pd.read_csv('data/ipl_matches_small.csv')
#Your Solution
def create_delivery_series():
    #data_df = pd.read_csv('data/ipl_matches_small.csv')
    value=pd.Series(ipl_matches_array[:,11])
    return value
    


pd.Series(ipl_matches_array[:,11])
data_df.info()
type(data_df['delivery'])


