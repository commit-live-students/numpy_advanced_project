# %load q01_get_total_deliveries_players/build.py
# Default imports
import pandas as pd
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman_name):
    DelDF = pd.read_csv('data/ipl_matches_small.csv')
#     batsmanCount = DelDF['batsman'].value_counts()
#     deli = batsmanCount[batsman_name]
    bats = (DelDF['batsman'] == batsman_name)
    bat = DelDF[bats]
    deliv = bat['batsman'].count()

    return deliv

batsman = input('enter batsman name')
get_total_deliveries_played(batsman)





