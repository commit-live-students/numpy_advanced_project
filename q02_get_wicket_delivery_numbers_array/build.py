#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def get_wicket_delivery_numbers_array(player):
    out = []
    for d in ipl_matches_array:
        if d[20] == player:
            out.append(d[11])
    return np.array(out)
