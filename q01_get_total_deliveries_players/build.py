# %load q01_get_total_deliveries_players/build.py
# Default imports
import pandas as pd
    
# Your Solution
def get_total_deliveries_played(batsman):
    batsman = batsman.decode('utf-8') 
    matches = pd.read_csv('data/ipl_matches_small.csv')
    sr_del =  matches.loc[matches['batsman']== batsman]
    no_of_deliveries = len(sr_del)
    return no_of_deliveries     





