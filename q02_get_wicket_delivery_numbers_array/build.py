#Default Imports
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
#ipl_matches_array = np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50",skip_header = 1, delimiter=",")
#Your Solution
def get_wicket_delivery_numbers_array(player_out):
    #player1 = DataFrame(ipl_matches_array[:, 19:20])
    rows = np.where(ipl_matches_array[:, 20:21] == player_out)
    #delivery = DataFrame(ipl_matches_array[:, 11:12])

    return ipl_matches_array[rows, 11][0]





print get_wicket_delivery_numbers_array(player_out = "ST Jayasuriya")
