#Default Imports
import numpy as np
import pandas as pd

def get_wicket_delivery_numbers_array(batsman):
    ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
    player_out = ipl_matches_array[0:,20]
    delivery_number = ipl_matches_array[0:,11]
    s = pd.Series(data = delivery_number, index = player_out)
    return s[batsman].values
