# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_wicket_delivery_numbers_array(player):
    player_out=ipl_matches_array[ipl_matches_array[:,-3]==player]
    if player_out!=[]:
        player_deliveries=player_out[:,11]
        return player_deliveries

player_out=ipl_matches_array[ipl_matches_array[:,-3]==b'SR Tendulkar']
player_deliveries=player_out[:,11]
player_deliveries


