# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    #data =ipl_matches_array[:,11]
    all_delivery=ipl_matches_array[:,11]
    batting_batsman = ipl_matches_array[:,13].astype(np.str)==batsman
    batsman_out=ipl_matches_array[:,-3].astype(np.str)==batsman
    return all_delivery[ batsman_out]
