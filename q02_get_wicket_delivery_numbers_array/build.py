# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
l=list(enumerate(ipl_matches_array[1,:]))

def get_wicket_delivery_numbers_array(player):
    a=ipl_matches_array[ipl_matches_array[:,20]==player]
    return a[:,11]
get_wicket_delivery_numbers_array('ST Jayasuriya')



c=['1','2','3']
b=np.array(c)
np.shape(b)

