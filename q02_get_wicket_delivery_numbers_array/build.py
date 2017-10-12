#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def get_wicket_delivery_numbers_array(player):
    out_delivery = []
    ipl_match = ipl_matches_array [:,[11,20]]
    out_delivery = ipl_match[ipl_match[:,1] == "ST Jayasuriya"]
    final_delivery = out_delivery[:,0]
    return final_delivery
