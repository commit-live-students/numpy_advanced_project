# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    result_array = np.array([])
    for i, x in enumerate(ipl_matches_array):
        if x[-3] == player:
            if len(x[-3])>2:
                result = x[11]
                result_array = np.append(result_array, result)
    return result_array
get_wicket_delivery_numbers_array(b'ST Jayasuriya')





