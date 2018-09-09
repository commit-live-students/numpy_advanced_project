# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array (player_out):
    return np.array(ipl_matches_array[:, [11, 20]][np.where(ipl_matches_array[:, [11, 20]][:,1] == player_out)][:,:1])


ipl_matches_array[:, [11, 20]][np.where(ipl_matches_array[:, [11, 20]][:,1] == b'ST Jayasuriya')][:,:1]





