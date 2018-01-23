#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team):
    toss_win = ipl_matches_array[:,[0,5]]
    match_codes = toss_win[toss_win[:,1]==team]
    ans = np.unique(match_codes[:,0])
    ans1 = int(ans.size)
    return ans1
