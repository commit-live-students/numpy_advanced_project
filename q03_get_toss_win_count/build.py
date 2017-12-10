#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
import pandas as pd

def get_toss_win_count(team):
    alltoss = ipl_matches_array[:,[0,5]]
    toss_won = alltoss[alltoss[:,1] == team]
    df = pd.DataFrame(toss_won)
    toss_count = df.groupby(df[:,1])
    return alltoss, toss_count

print get_toss_win_count("Mumbai Indians")
