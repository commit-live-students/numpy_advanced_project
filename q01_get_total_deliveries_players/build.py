import pandas as pd

str_path='data/ipl_matches_small.csv'

def read_ipl_data_csv(path):
    pd_series= pd.read_csv(path,  delimiter=',')
    return pd_series

def get_total_deliveries_played(batsman):
    batsman = 'SR Tendulkar'
    return series_ipl['batsman'].value_counts()[batsman]


series_ipl = read_ipl_data_csv(str_path)
int_batsman_deliveries = get_total_deliveries_played('fdsfdsfsdf fdfsdfds')
print('int_batsman_deliveries : ',int_batsman_deliveries)



