#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

team = 'Mumbai Indians'

def get_toss_win_count(team):
    #To get the records where Mumbai Indians had won the toss
    team_records = ipl_matches_array[ipl_matches_array[:, 5] == team]
    #To get the set of unique matches
    unique_matches = set(team_records[:, 0])
    return len(unique_matches)
