#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

def get_all_sixes_filter():
    #print ipl_matches_array[:,16:17]
    #print unique_matches
    #print ipl_matches_array[:,5]
    #sixes = np.where(ipl_matches_array[:,16]=='6')
    #print sixes
    #return np.unique(ipl_matches_array[rows,0][0]).shape[0]
    return ipl_matches_array[:,16]=='6'

print get_all_sixes_filter()
