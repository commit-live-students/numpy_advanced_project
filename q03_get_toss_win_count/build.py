#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team):

    match_code = ipl_matches_array[:,0][[ipl_matches_array[:,5] == team]]
    unq = np.unique(match_code)
    number_of_wins = int(unq.size)



    return number_of_wins





print get_toss_win_count('Mumbai Indians')
