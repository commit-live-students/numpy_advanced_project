# %load q05_create_delivery_series/build.py
#Default Imports
import numpy as np
import pandas as pd

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
#ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv",dtype="|S50",skip_header=1,delimiter=",")
#Your Solution
#delvry=[]
#a=[]
def create_delivery_series():
    # for i in range (len(ipl_matches_array)):
    #     delvry.append(ipl_matches_array[i][11])
    #     a=np.array(delvry)
    #     delivery =pd.Series(data=a)
    # return (delivery)
    delivery = pd.Series(ipl_matches_array[:,11])
    return (delivery)

create_delivery_series()
