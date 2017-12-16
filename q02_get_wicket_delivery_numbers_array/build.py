#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(player):
    sliced_delivery=ipl_matches_array[:,11:12]
    sliced_batsman_wicket=ipl_matches_array[:,20:21]
    data=np.hstack((sliced_delivery,sliced_batsman_wicket))
    deliveries=data[(np.where(data[:,1:]==player))]

    return deliveries
