# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
data = ipl_matches_array[:,13]
#print batsman

#print d

batsman = ''


def get_total_deliveries_played(batsman):
    unique, count = np.unique(data , return_counts= True)
    batsman_count = dict(zip(unique,count))
    return (batsman_count[batsman])

#print get_total_deliveries_played()
