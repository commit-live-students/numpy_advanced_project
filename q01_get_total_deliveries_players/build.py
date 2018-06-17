# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype=np.str, skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman): 
    batsman= len(ipl_matches_array[ipl_matches_array[:,13]==batsman])
    return batsman


get_total_deliveries_played('SR Tendulkar')


