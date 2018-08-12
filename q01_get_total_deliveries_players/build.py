# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
batsman='SR Tendulkar'
def get_total_deliveries_played(batsman):
    batsman_column=ipl_matches_array[:,13]
    no_of_occurance=np.where(batsman_column==batsman)
    total_deliveries_played=np.count_nonzero(no_of_occurance)
    return total_deliveries_played
