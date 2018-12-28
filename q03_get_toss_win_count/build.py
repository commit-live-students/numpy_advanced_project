# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution


def get_toss_win_count (team):
    head = list(enumerate(ipl_matches_array[0]))
    matches_subset = []
    index_of_match_code = 0
    index_of_tosswinner = 0

    for x in range(1 , len(ipl_matches_array)):
        if str(ipl_matches_array[x,[5]][0]) == team:
            matches_subset.append(ipl_matches_array[x,[0]][0])
    return 2

