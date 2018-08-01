# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
import pandas as pd

def get_all_sixes_filter():
    data = pd.read_csv('data/ipl_matches_small.csv')
    return data['runs'] == 6

