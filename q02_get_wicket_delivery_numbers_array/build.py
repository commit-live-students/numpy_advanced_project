#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
player='ST Jayasuriya'
def get_wicket_delivery_numbers_array(player):
    player_out=ipl_matches_array[:,11]
    deleveries=ipl_matches_array[:,20]
    player_out_deleveries_data=np.column_stack((player_out,deleveries))
    player_out_deleveries=player_out_deleveries_data[np.where(player_out_deleveries_data[:,1:]==player)]
    return player_out_deleveries
