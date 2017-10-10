import numpy as np
import pandas as pd
ipl_matches_array  =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(bat):
    index =ipl_matches_array[:,11].astype(np.float16)
    #print(index)
    values=ipl_matches_array[:,13].astype(np.str)

    delivery_bat=pd.Series(values,index)
    #print(delivery_bat)

    filter_bat =delivery_bat.values==bat
    #in_bat=0
    delivery_faced= len(delivery_bat[filter_bat])
    return delivery_faced
