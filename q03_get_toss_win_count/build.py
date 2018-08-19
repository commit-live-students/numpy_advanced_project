# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    count = 0
    matches = []
    for i in range(len(ipl_matches_array)):
        if ipl_matches_array[i][5] == team:
            matches.append(ipl_matches_array[i][0])
             
    return len(set(matches))

get_toss_win_count(b'Mumbai Indians')


