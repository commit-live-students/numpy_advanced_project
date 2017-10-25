#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_toss_win_count(team="Mumbai Indians"):
    l = [i[0] for i in ipl_matches_array if i[5] == team]
    return len(set(l))
