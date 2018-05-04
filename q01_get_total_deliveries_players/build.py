import pandas as pd
def get_total_deliveries_played(batsman_name):
    ipl_matches_array = pd.read_csv('data/ipl_matches_small.csv')
    return ipl_matches_array['batsman'].value_counts()[batsman_name]
get_total_deliveries_played('SR Tendulkar')




