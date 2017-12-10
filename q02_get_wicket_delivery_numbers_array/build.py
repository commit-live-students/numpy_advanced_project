#Default Imports
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
def get_wicket_delivery_numbers_array (player):
    #ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
    alldelv = ipl_matches_array[0:len(ipl_matches_array),[11,20]]
    wicket_delv = alldelv[alldelv[:,1] == player][:,0]
    return wicket_delv
