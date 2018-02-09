#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_all_sixes_filter():

    runs_array = ipl_matches_array[:,16]
    sixes_array = runs_array == '6'

    return sixes_array
