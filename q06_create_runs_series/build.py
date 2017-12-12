#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np
from pandas import Series


#Your Solution
def create_runs_series(match_code):
    match = ipl_matches_array[:, 0] == match_code
    runs = np.array(ipl_matches_array[:, 16])[match]
    delivery = np.array(ipl_matches_array[:, 11])[match]
    return Series(runs, delivery)
