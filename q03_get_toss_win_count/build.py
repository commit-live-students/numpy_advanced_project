#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_toss_win_count(s_team):
    i_cnt_toss_won = 0
    toss_winner_col_index = 5
    match_id_col_index = 0
    records_arr_toss_won = ipl_matches_array[ipl_matches_array[:,toss_winner_col_index]==s_team]
    i_cnt_toss_won = len(np.unique(records_arr_toss_won[:,match_id_col_index]))
    print "\nTeam {} won the toss {} times".format(s_team,i_cnt_toss_won)
    return i_cnt_toss_won
