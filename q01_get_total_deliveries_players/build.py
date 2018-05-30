# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution

def get_total_deliveries_played(batsman):
    deliveries=0
    bat=ipl_matches_array[:,-10]
    for cricketer in bat:
        if cricketer==batsman:
            deliveries+=1
    return deliveries
    



