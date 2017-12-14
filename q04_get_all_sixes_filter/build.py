# %load q04_get_all_sixes_filter/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

def get_all_sixes_filter():
    return ipl_matches_array[:,16].astype(np.int) == 6
