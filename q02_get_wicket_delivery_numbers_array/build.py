import numpy as np
import pandas as pd

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

out = ipl_matches_array[:, [11,20]]
#matches = np.unique(out[:,0])
delivery = []
#matches = np.unique(bats_delivery[:,0])
def get_wicket_delivery_numbers_array(player):
    for i,j in out:
        if j == player:
            delivery.append(i)
    return np.array(delivery)
