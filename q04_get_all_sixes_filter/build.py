# %load q04_get_all_sixes_filter/build.py
#Default Imports
#from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
path = "./data/ipl_matches_small.csv"

def get_all_sixes_filter():
    ipl_matches_array = np.genfromtxt(path,dtype='|S50',delimiter=',',skip_header=1)

    fliter_6 = ipl_matches_array[0:,16] == '6'
    #return np.unique(ipl_matches_array[fliter_6][0:,0])
    return fliter_6
