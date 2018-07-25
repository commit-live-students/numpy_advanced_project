import pandas as pd
import numpy as np


str_path='data/ipl_matches_small.csv'

def read_ipl_data_csv(path):
	pd_series= pd.read_csv(path,  delimiter=',' ,dtype='|S20')
	return pd_series

def get_total_deliveries_played(batsman):
	return series_ipl['batsman'].value_counts()[batsman]

	
def get_wicket_delivery_numbers_array(batsman):
	return np.array(series_ipl['delivery'][series_ipl['player_out'].str.contains(batsman) == True])

def get_toss_win_count(strTeam):
	#print (series_ipl['toss_winner'].str.contains('Mumbai Indians'))
	lst_toss_win = (series_ipl['match_code'][series_ipl['toss_winner'].str.contains(strTeam)].unique())
	int_toss= lst_toss_win.size
	return int_toss
	
	
series_ipl = read_ipl_data_csv(str_path)
#int_batsman_deliveries = get_total_deliveries_played('ST Jayasuriya')
#print('int_batsman_deliveries ; ',int_batsman_deliveries)
deliveries = get_wicket_delivery_numbers_array('ST Jayasuriya')
#print (series_ipl.groupby(['match_code','batsman','team1']).agg(np.sum).reset_index())
int_toss_win = get_toss_win_count('Mumbai Indians')
print (int_toss_win)


