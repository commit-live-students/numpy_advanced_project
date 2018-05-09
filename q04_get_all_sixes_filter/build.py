# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
import pandas as pd

ipl_matches_array =pd.read_csv('data/ipl_matches_small.csv')

def get_all_sixes_filter():
    return np.array(ipl_matches_array['runs'] == 6)

get_all_sixes_filter()



