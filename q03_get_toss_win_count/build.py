#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", delimiter=",", dtype="|S50", skip_header=1)

def get_toss_win_count(team):

    match_id = ipl_matches_array[:,[0,5]]
    unique_match = np.unique(match_id, axis = 0)
    print(unique_match)
    #unique_toss = np.unique(toss_array)
    #toss_list = zip(unique_toss,toss_count)
    #team_count = zip(unique_team,team_count)

    '''for ele in team_array:

        team_id,toss = ele
        if toss == team'''

get_toss_win_count('Mumbai Indians')
