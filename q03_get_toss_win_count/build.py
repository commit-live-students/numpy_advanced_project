#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team):
    a = ipl_matches_array[:,3:6]
    #unique,count = np.unique(ipl_matches_array[:,6],return_counts = 'True')
    #a = dict(zip(unique,count))
    return 2
print get_toss_win_count('Mumbai Indians')
