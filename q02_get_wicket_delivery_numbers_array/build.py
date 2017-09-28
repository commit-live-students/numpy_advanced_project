#Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..','..'))

from q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(player):
    wicket_filter = (ipl_matches_array[:, 20] == player)
    wickets_arr = ipl_matches_array[wicket_filter]
    return wickets_arr[:, 11]