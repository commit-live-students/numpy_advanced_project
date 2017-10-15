# %load q06_create_runs_series/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
match_code='392203'

#Your Solution
def create_runs_series(match_code):
    s1=ipl_matches_array[1:,[0,11,16]]
    s2=s1[s1[:,0]==match_code]
    #print(s2)
    series=pd.Series(s2[:,2],index=s2[:,1])
    #print(type(series))
    return(series)



create_runs_series (match_code)
