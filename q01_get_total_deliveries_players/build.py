# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman):
    name,occurence=np.unique(np.array(ipl_matches_array[:,-10].astype(str)), return_counts=True)
    return dict(list(zip(name,occurence)))[batsman]


