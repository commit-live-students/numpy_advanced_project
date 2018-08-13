#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def get_all_sixes_filter():

    array1=ipl_matches_array[:,16]
    k= (array1=='6')
    return k



#Your Solution
