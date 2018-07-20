# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
team = 'Mumbai Indians'
def get_toss_win_count(team):
    records = ipl_matches_array[ipl_matches_array[:,5] == team]
    matches = set(records[:,0])
    return len(matches)

print(get_toss_win_count(b'Mumbai Indians'))


