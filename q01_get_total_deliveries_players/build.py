# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=0, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman):
    
    #Storing the column of batsman into a separate list
    batsman_list = ipl_matches_array[1:,13]
        
    #Returning the count by making use of encode function as the data is unicode.
    return np.count_nonzero(batsman_list==batsman.encode())
    
#Call to the function.
get_total_deliveries_played('SR Tendulkar')





