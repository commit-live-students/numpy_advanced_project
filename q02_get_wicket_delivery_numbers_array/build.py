#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    data = ipl_matches_array

    x = np.array([i[11] for i in data if i[13] == batsman and i[20] == batsman])
    return x
