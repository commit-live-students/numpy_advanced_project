# %load q01_get_total_deliveries_players/build.py
# Default imports
import pandas as pd

def get_total_deliveries_played(batsman):
    ipl_matches_array = pd.read_csv('data/ipl_matches_small.csv')
    df = pd.DataFrame(ipl_matches_array)
    delivery_count = df.loc[df['batsman'] == 'SR Tendulkar']
    return delivery_count.shape[0]
    
get_total_deliveries_played('SR Tendulkar') 



# Your Solution



