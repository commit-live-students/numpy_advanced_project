#Default Imports
#from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
import pandas as pd
#Your Solution
ipl_matches_array =np.genfromtxt("/home/darshind/Workspace/code/numpy_advanced_project/data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_all_sixes_filter():
     return (ipl_matches_array[:, 16].astype(np.int16) == 6)
print get_all_sixes_filter()
