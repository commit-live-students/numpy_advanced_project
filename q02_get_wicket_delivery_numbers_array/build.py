import pandas as pd
import numpy as np


str_path='data/ipl_matches_small.csv'

def read_ipl_data_csv(path):
	pd_series= pd.read_csv(path,  delimiter=',', dtype='|S50')
	return pd_series

def get_total_deliveries_played(batsman):
	return series_ipl['batsman'].value_counts()[batsman]

	
def get_wicket_delivery_numbers_array(batsman):
	obj = np.array(series_ipl['delivery'][series_ipl['player_out'].str.contains(batsman) == True])
	print(type(obj))
	return obj
	
series_ipl = read_ipl_data_csv(str_path)
#int_batsman_deliveries = get_total_deliveries_played('ST Jayasuriya')
#print('int_batsman_deliveries ; ',int_batsman_deliveries)
deliveries = get_wicket_delivery_numbers_array('ST Jayasuriya')
print(type(deliveries))
#print (series_ipl.groupby(['match_code','batsman','team1']).agg(np.sum).reset_index())



