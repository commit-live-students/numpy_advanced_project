
import numpy as np
import pandas as pd
ipl_matches =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def create_delivery_series():
    return pd.Series(ipl_matches[:,11])
create_delivery_series()


