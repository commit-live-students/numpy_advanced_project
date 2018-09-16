# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=0, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    delivery_list = np.array([])
    for i,v in enumerate(ipl_matches_array):
        if ipl_matches_array[i][-3] == player.encode():
            #print(ipl_matches_array[i][11],ipl_matches_array[i][20])
            delivery_list = np.append(delivery_list,ipl_matches_array[i][11].decode())
    return delivery_list

get_wicket_delivery_numbers_array('SR Tendulkar')


a=np.array([])
print(a)


