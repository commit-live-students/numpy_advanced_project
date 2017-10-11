#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np
#from numpy import genfromtxt
def get_all_sixes_filter( ) :
    ipl_matches_array = pd.read_csv("./data/ipl_matches_small.csv", delimiter=',')
    #print ipl_matches_array.dtype.names
    #df[(df.a != -1) & (df.b != -1)]
    boolarr =  [(ipl_matches_array['runs'] == 6)]
    boolarr = np.array(boolarr)
    #ipl_matches_array[c == 'ST Jayasuriya',delievery]
    # count =  np.sum(boolarr)
    #a= ipl_matches_array[ipl_matches_array['runs'] == 6]
    #a = np.array(a, dtype=pd.Series)
    #a = ipl_matches_array[boolarr]
    return boolarr
#Your Solution
