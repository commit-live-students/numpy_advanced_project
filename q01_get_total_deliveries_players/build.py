# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
#ipl_matches_array.decode('utf-8')
# Your Solution
def get_total_deliveries_played(name):
    total_deliveries=0
    for i in range(0,len(ipl_matches_array),1):
        if str(ipl_matches_array[i,13], 'utf-8')==name:
            total_deliveries+=1
    return total_deliveries


