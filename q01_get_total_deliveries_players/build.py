# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    unique_batsman=np.unique(ipl_matches_array[:,13],return_counts=True)
    found_batsman = np.where(unique_batsman[0]==batsman)
    deliveries_batted=unique_batsman[1][found_batsman]
    #print(unique_batsman[0])
    #print(found_batsman)
    #print(deliveries_batted)
    return deliveries_batted
#print(get_total_deliveries_played('SR Tendulkar'))
