#Default Imports
#from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("/home/darshind/Workspace/code/numpy_advanced_project/data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution

def create_runs_series(match_code):
    data = ipl_matches_array[ipl_matches_array[:,0] == match_code]
    series = pd.Series(data[:,16], \
                       index=data[:,11])
    return series
print create_runs_series(match_code = '392203')
