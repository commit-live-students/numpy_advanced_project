#Default Imports
#from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("/home/darshind/Workspace/code/numpy_advanced_project/data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def create_delivery_series():
     return pd.Series(ipl_matches_array[:,11])
print create_delivery_series()
