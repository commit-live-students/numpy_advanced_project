#Default Imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

team_name = raw_input('Enter team ')
def get_toss_win_count(team_name):
    toss_winner = ipl_matches_array[:,5]
    match_code = ipl_matches_array[:, 0]
    s = pd.Series(data = match_code, index = toss_winner)
    winner = s[team_name].unique()
    return np.size(winner)

get_toss_win_count(team_name)
