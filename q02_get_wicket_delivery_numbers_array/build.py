#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(player):
    ipl_matches_array = np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
    deliveries = ipl_matches_array[:, (0,11,13,20) ] #matchcode,delivery number, batsman, batsman out
    filtered_indices = np.where(deliveries[:,3] == player)
    wicket_deliveries = deliveries[filtered_indices]
    return  wicket_deliveries [:,1]



    '''
    #to find out how many deliveries the player  has played
    filtered_indices = np.where(deliveries[:,2] == player)

    deliveries_faced= deliveries[zip(*filtered_indices)]

    matchcodes,deliveries_played= np.unique(deliveries_faced[:,0,0], return_counts= True)

    print deliveries_faced
    print deliveries_faced.shape
    print deliveries_faced.dtype


    
    print '-============'
    print matchcodes
    print deliveries_played
    return deliveries_played
    '''
