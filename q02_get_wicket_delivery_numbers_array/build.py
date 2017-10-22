#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
delivery = ipl_matches_array[:,11]
bats = ipl_matches_array[:,13]
out = ipl_matches_array[:,20]
def get_wicket_delivery_numbers_array(player):
    arr = []
    for i in delivery[out == player]:
        arr.append(i)
    return arr
