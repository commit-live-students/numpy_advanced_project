#Default Imports
import numpy as np
import pandas as pd

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(player):
    df = pd.DataFrame(ipl_matches_array)
    #print(df.head())
    df = df[[11,20]]
    find_player_filter = (df[20] == player)
    print(find_player_filter)
    print(df[find_player_filter])
    out_array = df[find_player_filter][11].values
    print(type(out_array))
    return out_array

    #print(df.head(30))
#get_wicket_delivery_numbers_array('ST Jayasuriya')
