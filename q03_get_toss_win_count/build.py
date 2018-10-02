# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
import pandas as pd


def get_toss_win_count(name):
    x= ipl_matches_array
    p=x[:,0]
    uni_teams,uni_index=np.unique(p,return_index=True)
    m=pd.DataFrame(x[:,[0,5]])
    t=[]
    for d in uni_index:
        t.append(m.get_value(d,1))  
        
    return t.count(name)
    
    
    
    
    #return x

#Your Solution


get_toss_win_count(b'Mumbai Indians')



















