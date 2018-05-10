# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


def create_runs_series(match_code): 
    indexDel=ipl_matches_array[:,11][ipl_matches_array[:,0].astype(str)==match_code]
    runs=ipl_matches_array[:,16][ipl_matches_array[:,0].astype(str)==match_code]
    return pd.Series(runs,index=indexDel)

#create_runs_series('392203')

