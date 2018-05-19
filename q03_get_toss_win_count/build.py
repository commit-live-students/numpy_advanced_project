# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np

import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_toss_win_count(team):
    data_df=pd.read_csv('data/ipl_matches_small.csv')
    value=len(data_df[['match_code','toss_winner']][data_df['toss_winner']==team]['match_code'].unique())
    return value

#Your Solution



