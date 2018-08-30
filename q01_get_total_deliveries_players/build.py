# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution

def get_total_deliveries_played(playerName):
    iplMatchDF = pd.read_csv('data/ipl_matches_small.csv')
    #print(iplMatchDF['batsman'].value_counts())
    batsmanCount = iplMatchDF['batsman'].value_counts()
    count = batsmanCount[playerName]
    return count

get_total_deliveries_played('SR Tendulkar')

