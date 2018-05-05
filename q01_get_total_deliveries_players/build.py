# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', skip_header=1,dtype= str,delimiter=',')
batsman= [b'SR Tendulkar']
# Your Solution
def get_total_deliveries_played(batsman):
    batsman_array = ipl_matches_array[:, 13]
    print(batsman_array)
    batsman_filter = batsman_array == batsman
   
    total_deliveries = len(ipl_matches_array[batsman_filter])
    
    return total_deliveries
get_total_deliveries_played(batsman)



