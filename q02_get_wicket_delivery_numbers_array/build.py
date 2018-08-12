#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_wicket_delivery_numbers_array(s_batsman):
    player_out_col_index = 20
    delivery_no_col_index = 11
    batsman_out_list = ipl_matches_array[ipl_matches_array[:,player_out_col_index]==s_batsman]
    batsman_out_delivery = batsman_out_list[:,delivery_no_col_index]
    print "\nBatsman out deliveries for batsman {} are : ".format(s_batsman),batsman_out_delivery
    return batsman_out_delivery
