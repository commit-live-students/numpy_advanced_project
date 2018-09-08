# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def create_delivery_series():
    deliveries=pd.Series(ipl_matches_array[:,11])
    return deliveries
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
balls_faced=ipl_matches_array[ipl_matches_array[:,13]==b'SC Ganguly']
deliveries=pd.Series(ipl_matches_array[:,11])
type(deliveries)



