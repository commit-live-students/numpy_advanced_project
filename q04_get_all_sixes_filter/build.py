#Default Imports
import numpy as np

def get_all_sixes_filter():
    ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
    Sixes = ipl_matches_array[0:,16].astype(np.int) == 6
    return Sixes


#Your Solution
