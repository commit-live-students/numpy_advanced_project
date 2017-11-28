#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(player):
    sliced_delivery=ipl_matches_array[:,11:12]
    sliced_batsman_wicket=ipl_matches_array[:,20:21]
    data=np.hstack((sliced_delivery,sliced_batsman_wicket))
    deliveries=data[(np.where(data[:,1:]==player))]

    return deliveries
