# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Define function to accept batsman as input which will be scanned in the array
# using for loop to check if the batsman is the same the increment the variable (number of deliveries played by 1)
def get_total_deliveries_played(batsman):
    variable=0
    for element in ipl_matches_array:
        if (element[13]==batsman):
            variable += 1

    return variable
