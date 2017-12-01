#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution
def get_all_sixes_filter():
    return ipl_matches_array[:,-7].astype(np.int16)==6
