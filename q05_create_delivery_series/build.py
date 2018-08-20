# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
l=list(enumerate(ipl_matches_array[0,:]))
print(l)
#Your Solution
def create_delivery_series():
    data=pd.Series(data=ipl_matches_array[:,11])
    return data
create_delivery_series()

