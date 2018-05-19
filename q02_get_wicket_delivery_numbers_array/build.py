# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_wicket_delivery_numbers_array(player):
    data_df=pd.read_csv('data/ipl_matches_small.csv')
    delivery_data_out=data_df[['batsman','player_out','delivery']][data_df['player_out']==player]
    return delivery_data_out['delivery']
    
#Your Solution


data_df=pd.read_csv('data/ipl_matches_small.csv')
data_df.info()
data_df[['batsman','player_out','delivery']][data_df['player_out']=='SR Tendulkar']
delivery_data_out=data_df[['batsman','player_out','delivery']][data_df['player_out']=='SR Tendulkar']
delivery_data_out['delivery']


