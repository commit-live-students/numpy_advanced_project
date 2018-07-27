# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_wicket_delivery_numbers_array(player):
    #make a list to answer the question
    out=[]
    #getting the required data wickets and overs
    info=ipl_matches_array[:,[11,20]]
    # 11 is for overs and 20 for player out column
    #fetching daata in loop
    for x in info:
        if x[1]  == player:
            out.append(x[0])
    return np.array(out)
    


get_wicket_delivery_numbers_array(b'SR Tendulkar')



