# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np

ipl_matches_array =pd.read_csv('data/ipl_matches_small.csv')

def create_delivery_series():
    return pd.Series(ipl_matches_array['delivery'])

#Your Solution

#create_delivery_series()


