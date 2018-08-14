# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team = 'Mumbai Indians'):
    toss_won = 0
    for x in ipl_matches_array:
        inning = int(x[10])
        delivery = float(x[11])
        toss_winner = str(x[5])
        if inning == 1 and delivery == 0.1 and team in toss_winner:
            toss_won = toss_won + 1
    toss_won = int(toss_won)
    return toss_won


