import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

# Using ipl_matches_array load the data in element (using for loop)
# Scan each element and check the toss_winner (column = 5) matches with the function parameter team
# if yes the load the match_code into numpy array and at the end of for koop get the unique count
# of numpy array using np.unique function and return the size
var = []
def get_toss_win_count(team):
    for element in ipl_matches_array:
        if element[5] == team:
            var.append(element[0])

        variable = np.unique(var, return_index=False, return_counts=True)[0]
    return np.size(variable)
