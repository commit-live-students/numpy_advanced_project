import pandas as pd

def get_total_deliveries_played(batsman):
    ipl_data=pd.read_csv('./data/ipl_matches_small.csv')
    deliveries=ipl_data['batsman']==batsman
    return int(deliveries.sum())
deliveries=get_total_deliveries_played('abc')
print(deliveries)


