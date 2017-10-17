#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution
def get_all_sixes_filter():
    sixes_filter = ipl_matches_array[:, -7 ].astype(np.int64) == 6
    return sixes_filter
