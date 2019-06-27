# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Funtion 
def create_delivery_series():
    ''' convert 1 darray to series '''
    deliveres_pd = pd.Series(ipl_matches_array[:,11])
    return deliveres_pd

#Function call
create_delivery_series()


