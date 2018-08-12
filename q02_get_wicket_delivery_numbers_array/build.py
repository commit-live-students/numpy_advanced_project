#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(player_out):
    arr = ipl_matches_array[:,(11,20)]
    delivery = arr[np.where(arr[:,1]==player_out)]
    return delivery[:,0]
