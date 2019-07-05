# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_toss_win_count(team):
    
    t_match=[]   
    info=ipl_matches_array[:,[0,5 ]]       
    for x in info:
        if x[1]  == team:
            t_match.append(x[0])
                         
    return len(np.unique(t_match))

get_toss_win_count(b'Mumbai Indians')




