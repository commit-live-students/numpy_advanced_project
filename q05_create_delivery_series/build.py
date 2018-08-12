#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
#df = pd.DataFrame(data,index=data[:,0]),
def create_delivery_series():
    deliveries=pd.Series(ipl_matches_array[:,11])
    #print type(deliveries)
    return deliveries

create_delivery_series()
