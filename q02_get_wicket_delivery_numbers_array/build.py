#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution

def get_wicket_delivery_numbers_array(parameter_list):
    filteredList=ipl_matches_array[:,:20]
    filteredIndex= (np.where(filteredList=='')[0])
    l=ipl_matches_array[:,20:21]
    wicketIndex= np.where(l==parameter_list)[0]
    o=ipl_matches_array[wicketIndex,11:12]
    return o[:,0]
