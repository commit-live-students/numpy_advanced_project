# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_delivery_series():
    
    #Pikcing up the column of delivery and passing it to series.
    Ser1 = pd.Series(ipl_matches_array[:,11])
    return Ser1

#Call to the function
create_delivery_series()




