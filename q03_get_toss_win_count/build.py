#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_toss_win_count(team):
    array=[]
    for delivery in ipl_matches_array:
        if(delivery[5]==team):
            array.append(delivery[0])
    return len(set(array))
