import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

# Using the loaded data from ipl_matches_array,
# Scan the "player_out" column -20 and compare the same with player (parameter passed in the function) and
# append the "delivery" column - 11 value to the list "variable" and return numpy array of variable

variable = list()
def get_wicket_delivery_numbers_array(player):
    for element in ipl_matches_array:
        if element[20] == player:
            list.append(variable, element[11])

    return np.array(variable)
