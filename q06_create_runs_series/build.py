# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np



#Your Solution
def create_runs_series(match_code=''):
    #ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    ipl_df= pd.read_csv('data/ipl_matches_small.csv')
    ipl_df=ipl_df[ipl_df['match_code'].astype(str)==match_code]
    ipl_df=ipl_df[['delivery','runs']]
    tmp= ipl_df.groupby(['delivery']).sum()
    return tmp['runs']
    

create_runs_series('392203')















