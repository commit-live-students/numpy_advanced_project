#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

import numpy as np
def get_toss_win_count(team="Mumbai Indians"):
    a=[]
    for i in ipl_matches_array:
        if i[5]=="Mumbai Indians":
            a.append(i[0])


    unique_matches = np.unique(a)

    count = len(unique_matches)
    return count
get_toss_win_count()
