from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
#Your Solution
def get_all_sixes_filter():
    return (ipl_matches_array[:, 16].astype(np.int16) == 6)
