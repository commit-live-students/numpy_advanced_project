#Default Imports
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution

def get_wicket_delivery_numbers_array(player):
    df_ipl_matches = DataFrame(ipl_matches_array)
    df_deliv_player = df_ipl_matches[[11,20]]
    return np.array(df_deliv_player[df_deliv_player[20]==player][11])
