
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team):
    #toss_winners = (ipl_matches_array[:,5])
    #match_days = (ipl_matches_array[:,1])
    D = ipl_matches_array[:,0][ipl_matches_array[:,5] == team]
    tosses_won = np.unique(D)



    return np.size(tosses_won)
