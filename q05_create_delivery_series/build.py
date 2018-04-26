# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
cols = ['match_code', 'date', 'city', 'team1', 'team2', 'toss_winner', 'toss_decision', 'winner','win_type',
        'win_margin', 'inning', 'delivery', 'batting_team', 'batsman', 'non_striker', 'bowler', 'runs', 'extras',
        'total', 'extras_type', 'player_out', 'wicket_kind', 'wicket_fielders']
#print (list(enumerate(cols)))


#Your Solution
def create_delivery_series():
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    res= pd.Series(ipl_matches_array[:,11])
    return (res)
    

create_delivery_series()

