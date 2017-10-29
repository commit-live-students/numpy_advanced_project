#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
#Your Solution
def get_toss_win_count(team = 'Mumbai Indians'):
    df = pd.DataFrame(ipl_matches_array)
    df = df[[0,5]]
    df.drop_duplicates(keep = 'first', inplace = True)
    df = df[5]
    count = df[(df == team)].count()
    #print(df.head())
    #print(count)
    return count
get_toss_win_count()
