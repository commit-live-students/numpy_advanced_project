#Default Imports
import numpy as np
import pandas as pd
from pandas import Series
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_all_sixes_filter():
    sixes = np.where(ipl_matches_array[:,16]=='6',True,False)
    return sixes

#print get_all_sixes_filter()
