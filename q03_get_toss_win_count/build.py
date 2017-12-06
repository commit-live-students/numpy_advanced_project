#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
#Your Solution
#First get the unique number of matches as an array. Pass that array as a filter to complete ipl array and slice only the toss_winner column.
#use numpy's count_nonzero to count the winner where the team is the team specified by input

def get_toss_win_count(team):
    return np.count_nonzero(ipl_matches_array[np.unique(ipl_matches_array[:,0], return_index = True)[1]][:,5] == team)
