# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_total_deliveries_played(batsman):
        ar2=list(ipl_matches_array[0:,13:14])
        count = 0
        for ele in ar2: 
            if (ele == batsman): 
                count = count + 1
        return count


get_total_deliveries_played(b'ST Jayasuriya')


