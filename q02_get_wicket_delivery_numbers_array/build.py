#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def get_wicket_delivery_numbers_array(batsman):
    deliveries_played=[]

    for i in ipl_matches_array:
        if ((i[13]==batsman) &(i[20]==batsman)):
            deliveries_played.append(i[11])

    wicket_delivery = np.array(deliveries_played)
    return wicket_delivery

get_wicket_delivery_numbers_array('ST Jayasuriya')
