# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    delivery = ipl_matches_array[:,11]
    runs = ipl_matches_array[:,18]
    series1 = pd.Series(data=runs,index=delivery)
    return series1


