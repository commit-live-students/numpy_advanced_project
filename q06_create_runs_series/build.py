# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series (match_code):   
    var = np.array(ipl_matches_array[:,:17])
    filterData = var[np.array([myfunc(row,match_code) for row in var])]
    return filterData[:,16:17]


# match_code = b'392203'
# var =ipl_matches_array[:,:16]


def myfunc(row,match_code):
    return row[0] == match_code





