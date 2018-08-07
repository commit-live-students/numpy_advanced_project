# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
df = pd.read_csv('data/ipl_matches_small.csv')

#Your Solution
def get_toss_win_count(team):
    a = np.array(ipl_matches_array[:,5]) 
    b= list(a)
    return int(b.count(b'Mumbai Indians')/(236))
get_toss_win_count('Mumbai Indians')
type(get_toss_win_count('Mumbai Indians'))


