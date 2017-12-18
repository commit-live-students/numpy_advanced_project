#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution
import pandas as pd
#Your Solution
def get_all_sixes_filter():
    return ipl_matches_array[:,16].astype(np.int16) == 6

#print get_all_sixes_filter()
