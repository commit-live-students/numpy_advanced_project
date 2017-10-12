#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
import numpy as np
def get_toss_win_count(team='Mumbai Indians'):
    unq_match_code = np.unique(ipl_matches_array[:, 0])
    count = 0
    for code in unq_match_code:
        match_filter = ipl_matches_array[:, 0] == code
        ball1 = ipl_matches_array[match_filter][0]
        if ball1[5] == team:
            count +=1
    return count
