import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_toss_win_count(teamname):
    return len(np.unique([elm[0] for elm in ipl_matches_array if elm[5] == teamname]))
