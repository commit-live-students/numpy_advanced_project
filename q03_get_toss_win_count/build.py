#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
import pandas as pd
import numpy as np
#from numpy import genfromtxt
def get_toss_win_count(team ="Mumbai Indians" ) :
    ipl_matches_array = pd.read_csv("./data/ipl_matches_small.csv", delimiter=',')
    #print ipl_matches_array.shape
    #print ipl_matches_array.dtype.names
    #df[(df.a != -1) & (df.b != -1)]
    #boolarr =  [(ipl_matches_array['batsman'] == batsman) & (ipl_matches_array['player_out'] == batsman)]
    #ipl_matches_array[c == 'ST Jayasuriya',delievery]
    # count =  np.sum(boolarr)
   # grp = ipl_matches_array.groupby(['match_code'])
    a = ipl_matches_array[ipl_matches_array['toss_winner'] == team]#.groupby(ipl_matches_array['match_code']).count()
    count =  a.groupby(ipl_matches_array['match_code']).agg('count')['match_code']
    count = count.count()

    #a = np.array(a, dtype=pd.Series)
    #a = ipl_matches_array[boolarr]
    #print boolarr
    return count
