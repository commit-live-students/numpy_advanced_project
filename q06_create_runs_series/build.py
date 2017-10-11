#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
#%load q06_create_runs_series/build.py

#%load q05_create_delivery_series/build.py

import pandas as pd
import numpy as np
from numpy import genfromtxt
def create_runs_series(match_code) :
    ipl_matches_array = ipl_matches_array = genfromtxt("./data/ipl_matches_small.csv", dtype = '|S20', delimiter=',', skip_header = 1)
    # = pd.read_csv("./data/ipl_matches_small.csv", delimiter=',')
    #df = ipl_matches_array.set_index('delivery') # Set index
    filt = ipl_matches_array[:,0] == str(match_code)
    df = ipl_matches_array[filt]

    #series = (df[['match_code','runs']])
    #series = df['runs']
    series = pd.Series(df[:,16],index = df[:,11])
    #series = pd.Series(series)
    #a= ipl_matches_array.loc[ipl_matches_array['player_out'] == player, 'delivery']
    #df = df.loc[df[:,'match_code','runs']]
    #print ipl_matches_array.dtype.names
    #df[(df.a != -1) & (df.b != -1)]
    #boolarr =  [(ipl_matches_array['runs'] == 6)]
    #boolarr = np.array(boolarr)
    #series = ipl_matches_array.loc[ipl_matches_array[:,delievery]]
    # count =  np.sum(boolarr)
    #a= ipl_matches_array['delivery']
    #a = np.array(a, dtype=pd.Series)
    #a = ipl_matches_array[boolarr]
    return series



#Your Solution
