#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


def get_all_sixes_filter():
    return ipl_matches_array[:,-7] == '6'
