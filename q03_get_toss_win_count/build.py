# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
import pandas as pd

def get_toss_win_count(team):
    df =pd.read_csv('data/ipl_matches_small.csv')
    pv=df[df['toss_winner']==team].groupby('match_code')
    variable=pv['toss_winner'].describe().count()[0].item()
    return variable


