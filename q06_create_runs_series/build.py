#Default Imports
import pandas as pd
import numpy as np
from pandas import Series

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def create_runs_series(match_code):

    # Get the runs column
    runs = ipl_matches_array[:,16]
    # Get the match_code column
    match = ipl_matches_array[:,0]
    # Create series of runs with match_code as index
    runs_series = Series(runs, index = match)
    # Get the runs for 1 particular match_code
    match_runs = runs_series.loc[match_code]
    # Get the delivery column
    delivery = ipl_matches_array[:,11]
    # Calculate the match_count's count, to fetch that many deliveries further
    count = match_runs.count()
    # Fetch all the deliveries for that particular match_id
    match_delivery = delivery[0:count]
    #Create a series of match_runs with index as delivery
    runs_series = Series(match_runs.values, index = match_delivery)

    return runs_series
