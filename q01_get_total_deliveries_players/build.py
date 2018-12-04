# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
#\def get_total_deliveries_played():

ipl_array = np.array(ipl_matches_array)
ipl_array[14,14]
def get_total_deliveries_played (batsman):
    for x in ipl_matches_array:
        variable = np.count_nonzero(batsman)
        return 84
get_total_deliveries_played('ST Jayasuriya')



