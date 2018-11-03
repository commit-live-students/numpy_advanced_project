# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd


ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution

def get_wicket_delivery_numbers_array(name):
    df=pd.DataFrame(ipl_matches_array[:,[11,-3]])
    x=df.loc[df[1] == name]
    y=np.array(x[0])
    return y
    
    
    
    
    
    

import pandas as pd

df=pd.DataFrame(ipl_matches_array[:,[11,-3]])
ipl_matches_array[:,[12,-3]]
list(df)
x=df.loc[df[1] == b'ST Jayasuriya']
np.shape(x)
y=np.array(x[0])
y
df



