import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
ipl_matches_array  = np.genfromtxt('./data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=",")
#Your Solution
def get_wicket_delivery_numbers_array(player):
    delivery= ipl_matches_array[0:,11]
    outfilter = ipl_matches_array[0:,20] == player
    return delivery[outfilter]
