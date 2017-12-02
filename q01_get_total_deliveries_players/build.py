# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman_name):
    filteredList= ipl_matches_array[:,13]
    filteredIndex= (np.where(filteredList==batsman_name)[0])
    return len(filteredIndex)
