# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    # condition
    c = ipl_matches_array[:,5].astype(str) == team
    # getting the team's winning of toss and then making a set of matches
    return len(set(ipl_matches_array[c][:,1]))

get_toss_win_count('Mumbai Indians')

