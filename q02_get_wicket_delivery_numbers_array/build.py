#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(player):
    #print(ipl_matches_array[0])
    player_out = np.where(ipl_matches_array[:,-3]==player)
    #print(player_out)
    return ipl_matches_array[player_out,11]
#print(get_wicket_delivery_numbers_array('K Goel'))
