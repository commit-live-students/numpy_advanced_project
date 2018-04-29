import pandas as pd
import numpy as np

def create_delivery_series():
    ipl_data=np.genfromtxt('./data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    return pd.Series(ipl_data[:,11])





