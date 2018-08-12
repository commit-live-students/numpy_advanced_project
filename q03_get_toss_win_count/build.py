#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(teams):
    toss_winning_team = np.where(ipl_matches_array[:,5]==teams)
    toss_winning_times=np.unique(ipl_matches_array[toss_winning_team,0]).size

    #print(toss_winning_team)
    return toss_winning_times
#print(get_toss_win_count('Mumbai Indians'))
