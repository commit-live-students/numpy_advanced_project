#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
from pandas import Series

#Create a numpy array using ipl_matches_array slicing feature for delivery and runs
#Using Series feature create Panda Series with delivery as Index and Runs as the corresponding value of those indices

def create_runs_series(match_code):

    delivery = ipl_matches_array[(ipl_matches_array[:,0] == match_code)][:,11]
    runs = ipl_matches_array[(ipl_matches_array[:,0] == match_code)][:,16]

    variable = pd.Series(runs, index=delivery)
    return variable
