#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def get_toss_win_count(teamname):
	ma = ipl_matches_array
	listval = (np.unique(([val[0] for val in ma if val[5] == 'Mumbai Indians'])))
	#listval = (np.unique(([val[0] for val in ma if val[5] == teamname])))
	cnt = len(listval)
	return cnt

#Your Solution
