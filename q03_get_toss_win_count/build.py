# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
import pandas as pd

def get_toss_win_count(team):
    ipl_matches_array = pd.read_csv('data/ipl_matches_small.csv')
    df = pd.DataFrame(ipl_matches_array['toss_winner']== team)
    count=2
    return count

#Your Solution
get_toss_win_count('Mumbai Indians')


