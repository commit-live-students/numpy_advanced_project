# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
cols = ['match_code', 'date', 'city', 'team1', 'team2', 'toss_winner', 'toss_decision', 'winner','win_type',
        'win_margin', 'inning', 'delivery', 'batting_team', 'batsman', 'non_striker', 'bowler', 'runs', 'extras',
        'total', 'extras_type', 'player_out', 'wicket_kind', 'wicket_fielders']
list(enumerate(cols))

#Your Solution
def get_all_sixes_filter():
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    runs= ipl_matches_array[:,16].astype(np.int16)
    res= runs == 6
    return res
    

