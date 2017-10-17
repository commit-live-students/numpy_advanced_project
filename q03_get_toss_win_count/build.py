#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_toss_win_count(team="Mumbai Indians"):
    count = 0
    match_set = set()

    for item in ipl_matches_array:
        match_set.add(item[0])

    for match in match_set:
        for item in ipl_matches_array:
            if item[0] == match and item[5] == team:
                count +=1
                break
    return count
