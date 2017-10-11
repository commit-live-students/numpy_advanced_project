# Default imports
#import numpy as np

#ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

import pandas as pd
import numpy as np
#from numpy import genfromtxt
def get_total_deliveries_played(batsman) :
    ipl_matches_array = pd.read_csv("./data/ipl_matches_small.csv", delimiter=',')
    #print ipl_matches_array.dtype.names
    boolarr =  ipl_matches_array['batsman'] == batsman
    count =  np.sum(boolarr)
    return count
# Your Solution
