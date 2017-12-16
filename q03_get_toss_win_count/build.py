#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team):
    sliced_toss_winner=ipl_matches_array[:,5:6]
    count=len(sliced_toss_winner[(np.where((sliced_toss_winner==team,1)))])
    return count
