# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=0, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    toss_count = 0
    for i,v in enumerate(ipl_matches_array):
        if ipl_matches_array[i][5]==team:
            #print(ipl_matches_array[i][6])
            toss_count += 1
    return toss_count
    #print(ipl_matches_array[0,6])
    
get_toss_win_count(b'Mumbai Indians')

ipl_matches_array[0,5]
ipl_matches_array[1,5]



