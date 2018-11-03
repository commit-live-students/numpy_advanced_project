# %load q03_get_toss_win_count/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_toss_win_count(team):
    return len(set(ipl_matches_array[ipl_matches_array[:,5]==team][:,0]))


get_toss_win_count(b'Mumbai Indians')


