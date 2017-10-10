#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution
def get_all_sixes_filter():
    flt_six = ipl_matches_array[:,16].astype(np.float16) == 6
    #match_six = ipl_matches_array[flt_six]
    #match_num = np.unique(match_six[:,0])
    return flt_six
