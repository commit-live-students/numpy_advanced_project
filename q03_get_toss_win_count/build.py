#Default Imports

import numpy as np
import pandas as pd

def get_toss_win_count(team_name):
    ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
    toss_winner = ipl_matches_array[0:,5]
    match_code = ipl_matches_array[0:,0]
    s = pd.Series(data=match_code, index = toss_winner)
    winning_matches = s[team_name].unique()
    return np.size(winning_matches)


#Your Solution
