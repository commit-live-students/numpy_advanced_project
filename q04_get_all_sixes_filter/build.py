# %load q04_get_all_sixes_filter/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution
def get_all_sixes_filter():
    fil1=ipl_matches_array[:,16].astype(np.float16)==6
    #print(ipl_matches_array[fil1,16])
    #print(fil1)
    return fil1
#get_all_sixes_filter()
