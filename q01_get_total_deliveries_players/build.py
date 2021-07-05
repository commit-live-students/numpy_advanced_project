# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution

def get_total_deliveries_played(batsman):
    no_of_deliveries=0
    for x in ipl_matches_array:
        if x[13]==batsman:
            no_of_deliveries=no_of_deliveries+1
    
    #print (no_of_deliveries)
    return no_of_deliveries

#get_total_deliveries_played(b'SR Tendulkar')




