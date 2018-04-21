# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_all_sixes_filter():
    c = ipl_matches_array[:,-7].astype(dtype=np.int) == 6
    return c

import pandas as pd
d = pd.read_csv('data/ipl_matches_small.csv')
d.columns
d.head()


