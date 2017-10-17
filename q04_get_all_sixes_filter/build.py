# %load q04_get_all_sixes_filter/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution
def get_all_sixes_filter():
    sixFilter=(ipl_matches_array[:,16].astype(np.int16)==6)
    return sixFilter

get_all_sixes_filter()
