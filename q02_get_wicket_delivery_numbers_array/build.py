# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_wicket_delivery_numbers_array(player):
    #making list for this function 
    out=[]
    #getting match info 
    info=ipl_matches_array[:,[11,20]]
    #find the name of player in info 
    for x in info:
        if x[1]==player:
            out.append(x[0])
    return np.array(out)
    

#Your Solution





