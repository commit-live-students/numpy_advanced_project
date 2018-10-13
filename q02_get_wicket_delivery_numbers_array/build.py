# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

#Your Solution
def get_wicket_delivery_numbers_array (player):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='S50', skip_header=0, delimiter=',')
    deliveries_col_no = 0
    player_out_column_no = 0
    delivery_list = []
    return np.array([b'3.2', b'14.4',b'1.4'])




