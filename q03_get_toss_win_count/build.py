# %load q03_get_toss_win_count/build.py
#Default Imports
import pandas as pd
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
y=0
#Your Solutio
#def get_toss_win_count(str):
#def get_toss_win_count(team):
def get_toss_win_count(team='Mumbai Indians'):
    fil1=ipl_matches_array[:,5]==team
    y=ipl_matches_array[fil1,0]
    return len(np.unique(y))
#get_toss_win_count(team='Mumbai Indians')
