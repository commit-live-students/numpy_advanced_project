# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
match_code=b'392203'

def create_runs_series(match_code):
    
    mac_del_runs_array=ipl_matches_array[:,[0,11,16]]
    
    mac_filter=(mac_del_runs_array[:,0]==match_code)
    #print(mac_del_runs_array[mac_filter])
    
    delivery=mac_del_runs_array[mac_filter][:,1]
    runs=mac_del_runs_array[mac_filter][:,2]
    
    runs_series=pd.Series(runs,index=delivery)
    
    return runs_series

create_runs_series(match_code)




