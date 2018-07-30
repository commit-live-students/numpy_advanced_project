# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np

#Your Solution
def create_delivery_series():
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    a=pd.Series(ipl_matches_array[:,11])
    return type(a)
    


b=create_delivery_series()
b


