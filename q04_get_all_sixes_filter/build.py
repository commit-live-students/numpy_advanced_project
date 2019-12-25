# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
#Your Solution
def get_all_sixes_filter():
    ipl_match = pd.read_csv('data/ipl_matches_small.csv')
    six_filter = (ipl_match['runs']==6).values
    return six_filter


