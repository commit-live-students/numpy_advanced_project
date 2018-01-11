#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    ball = ipl_matches_array[:,11:12]
    wicket = ipl_matches_array[:,20:21]
    pair = np.hstack((ball, wicket))
    return pair[(np.where(pair[:,1:]==batsman))]
