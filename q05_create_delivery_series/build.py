#Default Imports
#import pandas as pd
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np
from numpy import genfromtxt
#from numpy import genfromtxt
def create_delivery_series() :
    ipl_matches_array = ipl_matches_array = genfromtxt("./data/ipl_matches_small.csv", dtype = '|S20', delimiter=',', skip_header = 1)
    #print ipl_matches_array.dtype.names
    #df[(df.a != -1)
   # & (df.b != -1)]
    #boolarr =  [(ipl_matches_array['runs'] == 6)]
    #boolarr = np.array(boolarr)
    #a = ipl_matches_array[ipl_matches_array['batsman'] == 'ST Jayasuriya']
    #series = ipl_matches_array['delivery']
    # count =  np.sum(boolarr)
    #a= ipl_matches_array[ipl_matches_array['runs'] == 6]
    #a = np.array(a, dtype=pd.Series)
    #a = ipl_matches_array[boolarr]
    return pd.Series(ipl_matches_array[:,11])
#Your Solution
