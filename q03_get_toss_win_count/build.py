#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
#Your Solution
def get_toss_win_count(team='Mumbai Indians'):
    match_code=ipl_matches_array[:,0]
    filter_team=(ipl_matches_array[:,5]==team)

    return len(np.unique(match_code[filter_team]))

get_toss_win_count('Mumbai Indians')
