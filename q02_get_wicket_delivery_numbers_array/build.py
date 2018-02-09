# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_wicket_delivery_numbers_array(got_out):
    player_out = ipl_matches_array[:, [11,20]]
    out_player = player_out[player_out[:,1]==got_out]
    final = out_player[:,0]
    return final


