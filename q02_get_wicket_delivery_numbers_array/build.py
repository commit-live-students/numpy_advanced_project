# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
#11th col = delivery , -3th col = player_out
def get_wicket_delivery_numbers_array(player):
    x=[]
    x=np.where(ipl_matches_array[:,-3]==player)
    return ipl_matches_array[x,11]
get_wicket_delivery_numbers_array(b'ST Jayasuriya')


