# %load q06_create_runs_series/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
#11 TH INDEX IS DELIVERY
#def create_runs_services(match_code):
#print(type(ipl_matches_array))
#print(ipl_matches_array[0:2,:])
def create_runs_series(match_code):
    #print(ipl_matches_array[0:2,:])
    fil1=(ipl_matches_array[:,0]==match_code)
    #print(len(fil1))
    #print(len(ipl_matches_array))
    hi=ipl_matches_array[fil1,:]
    series=pd.Series(hi[:,16],hi[:,11])
    #print(series)
    #print(type(series))
    return series
#Your Solution
#create_runs_series("392203")
