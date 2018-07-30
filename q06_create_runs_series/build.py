# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    ipl_data=ipl_matches_array[:,[0,11,16]]
    ipl_df=pd.DataFrame(ipl_data)
    ipl_df=ipl_df.loc[ipl_df[0]==match_code]
    ipl_series=pd.Series(ipl_df[2].values,index=ipl_df[1])
    return ipl_series
create_runs_series(b'392203')



