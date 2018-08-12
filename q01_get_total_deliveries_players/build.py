# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
#Enumerating the columns

cols = ['match_code', 'date', 'city', 'team1', 'team2', 'toss_winner', 'toss_decision', 'winner','win_type',
        'win_margin', 'inning', 'delivery', 'batting_team', 'batsman', 'non_striker', 'bowler', 'runs', 'extras',
        'total', 'extras_type', 'player_out', 'wicket_kind', 'wicket_fielders']
a=list(enumerate(cols))





# Your Solution
def get_total_deliveries_played(batsman):

    count=0
    for batter in ipl_matches_array[:,13]:
        if batter==batsman:
            count+=1

    return count
