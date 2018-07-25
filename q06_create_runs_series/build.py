# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
match_code = b'392203'

#Your Solution
def create_runs_series(match_code):
    ipl_matches_filter = (ipl_matches_array[:,0]==match_code)
    ipl_match =  ipl_matches_array[ipl_matches_filter]
    Pandas_Series = pd.Series(index=ipl_match[:,11],data=ipl_match[:,16])
    return Pandas_Series
create_runs_series()


