# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman):
    
    
    data_of_batsman = ipl_matches_array[:,13] # to store batsman column data


    total_number_of_deliveries = len(data_of_batsman[ data_of_batsman == batsman])
    return total_number_of_deliveries
    

player_name = 'SR Tendulkar'.encode()
get_total_deliveries_played(player_name)




