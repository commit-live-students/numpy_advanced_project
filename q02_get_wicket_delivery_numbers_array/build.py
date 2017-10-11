#Default Imports
import pandas as pd
import numpy as np
#from numpy import genfromtxt
def get_wicket_delivery_numbers_array(player) :
    ipl_matches_array = pd.read_csv("./data/ipl_matches_small.csv", delimiter=',')
    #print ipl_matches_array.dtype.names
    #df[(df.a != -1) & (df.b != -1)]
    #boolarr =  [(ipl_matches_array['batsman'] == batsman) & (ipl_matches_array['player_out'] == batsman)]
    #ipl_matches_array[c == 'ST Jayasuriya',delievery]
    # count =  np.sum(boolarr)
    a= ipl_matches_array.loc[ipl_matches_array['player_out'] == player, 'delivery']
    a = np.array(a, dtype=pd.Series)
    #a = ipl_matches_array[boolarr]
    #print boolarr
    return a
