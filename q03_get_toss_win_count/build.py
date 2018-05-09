# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
import pandas as pd

ipl_matches_array =pd.read_csv('data/ipl_matches_small.csv')

def get_toss_win_count(team):
    return ipl_matches_array[ipl_matches_array['toss_winner'] == team]['match_code'].nunique()

#Your Solution
get_toss_win_count('Mumbai Indians')



