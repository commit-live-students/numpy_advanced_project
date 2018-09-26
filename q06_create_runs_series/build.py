#%load q06_create_runs_series/build.py

import pandas as pd
import numpy as np


path='./data/ipl_matches_small.csv'

def create_runs_series(match_code):
    arr=np.genfromtxt(path,skip_header=1,dtype='|S50',delimiter=',')
    #arr1=arr[:,0]
    #arr2=arr1[arr1==392203]arr
    arr2=(arr[:,0]==match_code)
   #arr1[arr1==392203]

    delivery=arr[:,11][arr2]
    runs=arr[:,16][arr2]

    sr1=pd.Series(runs,delivery)

    return(sr1)


create_runs_series(b'392203')





