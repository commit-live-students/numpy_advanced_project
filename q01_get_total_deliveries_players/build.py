# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution

def get_total_deliveries_played(batsman=b'SR Tendulkar'):#function buileded with default parameter batsman
    batsman_total=ipl_matches_array[:,13:14] #accessing the batsman column from the array for the count
    batsman_ball_faced=list(batsman_total).count(b'SR Tendulkar') #getting the count of the of the batsman
    return(batsman_ball_faced)
    
get_total_deliveries_played()







