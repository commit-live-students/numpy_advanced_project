from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
#Your Solution
def create_runs_series (match_code):
    match_code_filter = ipl_matches_array[:,0] == str(match_code)
    new_df = ipl_matches_array[match_code_filter]
    series = pd.Series(new_df[:,16], index=new_df[:,11])
    return series
