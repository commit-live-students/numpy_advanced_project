from pandas import Series, DataFrame
import pandas as pd
import numpy as np
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#ipl_matches_array = np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", delimiter=",")

#Your Solution
def create_runs_series(matches_code):
    rows = np.where(ipl_matches_array[:,0] == matches_code)
    matches_cd = pd.Series(data = ipl_matches_array[rows, 16][0], index = (ipl_matches_array[rows, 11][0]))
    #print type(matches_cd)
    return matches_cd
print create_runs_series(matches_code = '392203')
