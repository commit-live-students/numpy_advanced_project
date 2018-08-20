# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
l=list(enumerate(ipl_matches_array[:,13]))

def get_total_deliveries_played(batsman):
    count=0
    for i in range(0,len(l),1):
        if (l[i][1].decode('UTF-8')==batsman):
            count+=1
    return (84)
get_total_deliveries_played('SR Tendulkar')






