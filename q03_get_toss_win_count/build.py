# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
Team_Name = 'Mumbai Indians'

#Your Solution
def get_toss_win_count(Team_Name):
    df = pd.read_csv('data/ipl_matches_small.csv')
    df1 = df[df['toss_winner']==Team_Name]['match_code'].drop_duplicates()
    return len(df1.index)
Team_Name = 'Mumbai Indians'
get_toss_win_count(Team_Name)


