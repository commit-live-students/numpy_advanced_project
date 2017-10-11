#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

def get_all_sixes_filter():


    sixes_filter = ipl_matches_array[:,16].astype(np.int)==6
    return sixes_filter


get_all_sixes_filter()
