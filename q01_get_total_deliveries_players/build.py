# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def myfunc(row,name):
    return row[1] == name

# Your Solution
def get_total_deliveries_played(name):
    var = np.array(ipl_matches_array[:,[11,13]])
    return np.count_nonzero(var[np.array([myfunc(row,name) for row in var])][:,[0]])



