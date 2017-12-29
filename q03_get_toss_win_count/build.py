#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

import pandas as pd
#Your Solution
def get_toss_win_count(team):
    base_df = pd.DataFrame(ipl_matches_array)
    my_df = base_df[[0,5]]
    toss_win_teams = my_df.groupby([5])[0].nunique()
    return int(toss_win_teams[team])
print get_toss_win_count('Mumbai Indians')
