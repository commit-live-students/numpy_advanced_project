# %load q04_get_all_sixes_filter/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution

def get_all_sixes_filter():

    all_sixes=ipl_matches_array[:,16].astype(np.int16)==6
    #print(all_sixes)
    return all_sixes
    #print
