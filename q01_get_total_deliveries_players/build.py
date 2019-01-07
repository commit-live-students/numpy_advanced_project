# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd

ipl_matches_array=pd.DataFrame(np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=','))
batmans = list(ipl_matches_array[13])
non_strike = list(ipl_matches_array[14])
decoded_batsman = [item for item in batmans]
decoded_non_strike = [item for item in non_strike]

def get_total_deliveries_played(p_batsman):
    return decoded_batsman.count(p_batsman)
get_total_deliveries_played('ST Jayasuriya')
ipl_matches_array.tail()



