#Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..','..'))

from q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_toss_win_count(team='Mumbai Indians'):
    team_records = ipl_matches_array[ipl_matches_array[:, 5] == team]
    unique_matches = set(team_records[:, 0])
    return len(unique_matches)