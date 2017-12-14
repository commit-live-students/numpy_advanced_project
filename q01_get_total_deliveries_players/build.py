# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    all_batsman = ipl_matches_array[:,13] # Read batsman column

    # Get batsman and count
    batsman_name, count = np.unique(all_batsman, return_counts=True)

    # Combine both the output lists into a tuple set
    batsman_deliveries = dict(zip(batsman_name, count))

    # Get the count from the dict for given name
    return batsman_deliveries[batsman]

#print 'Morkel: {0}'.format(get_total_deliveries_played('JA Morkel'))
#print 'Yuvraj: {0}'.format(get_total_deliveries_played('Yuvraj Singh'))
