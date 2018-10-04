# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    team1 = np.unique(ipl_matches_array[:,4])
    team2= np.unique(ipl_matches_array[:,5])
    win_toss= ipl_matches_array[:,6]
    a =len(team1[team1==team ])
    b= len(team2[team2==team])
    
    return (a+b)
get_toss_win_count(b'Mumbai Indians')


