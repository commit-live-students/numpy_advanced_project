#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
import numpy as np

def get_toss_win_count(team='Mumbai Indians'):
    ipl_matches_array = np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
    toss_winners =  ipl_matches_array[:,(0,5)]
    filtered_index= np.where  (toss_winners[:,1]==team)
    matchcodes_where_toss_won= toss_winners[filtered_index][:,0]
    return  len(np.unique(matchcodes_where_toss_won))
