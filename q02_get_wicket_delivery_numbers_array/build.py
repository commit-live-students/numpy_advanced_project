# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    data = ipl_matches_array[ipl_matches_array[:,20] == batsman]
    return data[:,11]

get_wicket_delivery_numbers_array('SR Tendulkar')

import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_wicket_delivery_numbers_array(player):
    out=[]
    info = ipl_matches_array[:,[11,20]]
    for x in info:
        if x[1] == player:
            out.append(x[0])
    return np.array(out)
get_wicket_delivery_numbers_array(b'SR Tendulkar')



