# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution

def get_wicket_delivery_numbers_array (player):
    '''Approach 1 - Read data set in pandas. Use index method to find column positions instead of manually counting it
    Convert player_out and delivery column to list
    Iterate through player_out column and when the value == player, extract that position value from delivery list and make a new list
    '''
    dataset = pd.read_csv('data/ipl_matches_small.csv')
    header_list = list(dataset)
    player_out_list = ipl_matches_array[1:,header_list.index('player_out')].tolist()
    delivery_list = ipl_matches_array[1:,header_list.index('delivery')].tolist()
    deliveries = []
    for pos, player_out in enumerate(player_out_list):
        if (player_out == player):
            deliveries.append(delivery_list[pos])
    deliveries = np.array(deliveries)
        
    '''Approach 2 - Using loc method in pandas
    '''
    #print(dataset['player_out'])
    #numpylist = ipl_matches_array[1:,header_list.index('player_out')]
    delivery_list = dataset.loc[dataset['player_out']==player, ['delivery']]

    
    '''Approach 3 - Using numpy    
    '''
    player_out_delivery_df = ipl_matches_array[0:,(header_list.index('player_out'), header_list.index('delivery'))]
    delivery_list = player_out_delivery_df[np.where(player_out_delivery_df[:,0]==player), 1]
    return delivery_list

get_wicket_delivery_numbers_array(b'ST Jayasuriya')


