#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_wicket_delivery_numbers_array(playername):
    n1 = np.where(ipl_matches_array[:,-3]==playername)
    return ipl_matches_array[n1,-12]
