#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def get_all_sixes_filter():
    filter1 = ipl_matches_array[:,16].astype(np.int16) == 6
    sixer_match = ipl_matches_array[filter1]
    return sixer_match
