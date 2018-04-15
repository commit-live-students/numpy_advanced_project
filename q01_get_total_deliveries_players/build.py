# %load q01_get_total_deliveries_players/build.py
# Default imports
import pandas as pd

ipl_matches_array =pd.read_csv('data/ipl_matches_small.csv')

def get_total_deliveries_played(batsman):
    df=ipl_matches_array['batsman'].value_counts()
    count=df[batsman]
    return count
# get_total_deliveries_played('SR Tendulkar')





