# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
import pandas as pd

def get_toss_win_count(team):
    data = pd.read_csv('data/ipl_matches_small.csv')
    return data[data['toss_winner'] == team]['match_code'].unique().size




