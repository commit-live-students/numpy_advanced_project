# %load q01_get_total_deliveries_players/build.py

import pandas as pd
path = 'data/ipl_matches_small.csv'
data = pd.read_csv(path)
def get_total_deliveries_played(batsman):
    a = data['winner'][data['batsman']==batsman].count()
    return a
