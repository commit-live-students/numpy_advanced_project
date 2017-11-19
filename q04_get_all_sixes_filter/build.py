#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution
def get_all_sixes_filter():
    array = ipl_matches_array[:,:]
    ar = array[array[:,16].astype(np.int16) == 6]
    return ar
