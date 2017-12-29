# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    allbatsman = ipl_matches_array[:,13]  # Read batsman column

    # Get batsman and count
    batsman_name, count = np.unique(allbatsman, return_counts=True)

    # Combine both the output lists into a tuple set
    deliveries = dict(zip(batsman_name, count))
    return deliveries[batsman]
