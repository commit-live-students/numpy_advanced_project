#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
import pandas as pd
def get_toss_win_count(team):
    base_df = pd.DataFrame(ipl_matches_array)
    my_df = base_df[[0,5]]
    #print my_df
    toss_win_teams = my_df.groupby([5])[0].nunique()
    #print toss_win_teams
    return int(toss_win_teams[team])

#print get_toss_win_count('Mumbai Indians')
#print type(get_toss_win_count('Mumbai Indians'))
