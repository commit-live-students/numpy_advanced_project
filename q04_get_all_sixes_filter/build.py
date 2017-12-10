#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
def get_all_sixes_filter():
    allruns = ipl_matches_array[0:len(ipl_matches_array),16].astype(np.int16)
    sixes = allruns==6#[allruns == '6']
    return sixes
