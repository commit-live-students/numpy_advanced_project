# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(matchcode):
    a=ipl_matches_array
    d=[]
    c=[]
    for i in range(len(a)):
        if (a[i][0])==matchcode:
            b=a[i][16].astype(np.int)
            d.append(b)
            e=a[i][11]
            c.append(e)
    
    f=pd.Series(d,index=c)
    return f
        #a=(iplmatches_array[:,16]).astype(np.int16)#runs
    #b=(ipl_matches_array[:,11]).astypefloat)#deliveries
    



c=create_runs_series(b'392203')
type(c)


