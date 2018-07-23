# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    matach_data = ipl_matches_array[:,[11,20]]
    wicket_delivery=[]
    for data in matach_data:
        if data[1] == player:
            wicket_delivery.append(data[0])
    return np.array(wicket_delivery)

print(get_wicket_delivery_numbers_array(b'ST Jayasuriya'))





