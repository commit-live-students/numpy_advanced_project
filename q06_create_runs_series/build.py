
import numpy as np
import pandas as pd

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
#Your Solution
def create_runs_series(match_code):
    match = ipl_matches_array[ipl_matches_array[:, 0] == match_code]
    return pd.Series(match[:, 16], index=match[:, 11])

create_runs_series(b'392203')



