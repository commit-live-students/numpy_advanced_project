# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array (player_out):
    return np.array(ipl_matches_array[:, [11, 20]][np.where(ipl_matches_array[:, [11, 20]][:,1] == player_out)][:,:1]).flatten().astype('|S4')
player_out = b'ST Jayasuriya'

np.array(ipl_matches_array[:, [11, 20]][np.where(ipl_matches_array[:, [11, 20]][:,1] == player_out)][:,:1]).astype('|S4')
np.array([b'3.2', b'14.4',b'1.4'])
deliveries = get_wicket_delivery_numbers_array(b'ST Jayasuriya')
np.all(deliveries == np.array([b'3.2', b'14.4',b'1.4']))




