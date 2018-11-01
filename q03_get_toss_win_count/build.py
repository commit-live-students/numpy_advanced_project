# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    toss_win_match=[]
    ipl=ipl_matches_array[:,[0,5]]
    for matches in ipl:
        if matches[1] == team:
            toss_win_match.append(matches[0])
    return int(len(set(toss_win_match)))    
get_toss_win_count(b'Mumbai Indians')



