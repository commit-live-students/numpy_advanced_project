#Default Imports
import pandas as pd
import numpy as np
from pandas import Series

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def create_runs_series(match_code):

    runs = ipl_matches_array[:,16]
    match = ipl_matches_array[:,0]
    runs_series = Series(runs, index = match)
    match_runs = runs_series.loc['392203']
    count = match_runs.count()
    delivery = ipl_matches_array[:,11]
    match_delivery = delivery[0:count]
    runs_series = Series(match_runs.values, index = match_delivery)

    return runs_series
