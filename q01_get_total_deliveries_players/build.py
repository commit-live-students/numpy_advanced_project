# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
     no_of_deliveries = 0

     for i in ipl_matches_array[:,13]:
         if i == batsman:
             no_of_deliveries = no_of_deliveries + 1

     return no_of_deliveries
