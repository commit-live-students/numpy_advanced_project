#Default Imports
import pandas as pd
import numpy as np
from pandas import Series
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

match_code = ''

def create_runs_series(match_code):
    a = ipl_matches_array
    required_data =  a[a[:,0] == match_code]
    #print e
    runs_column = required_data[:,16]
    delivery_column = required_data[:,11]
    #print runs_column
    #print delivery_column

    required_series = Series(runs_column , index=delivery_column)
    return required_series


print create_runs_series(match_code)
