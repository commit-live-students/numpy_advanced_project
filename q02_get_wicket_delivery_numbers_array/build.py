# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(players):
    data=pd.DataFrame(ipl_matches_array)
    player=bytes(players,'utf8')
    d1=data[20]
    #print(player,data[20][21])
    #print(np.where(d1==player))
   
    #print(data[d1==player][11])
    arr=np.array(data[d1==player][11])
    #arr=arr.astype(float)
    #print(type(arr))
    return(arr)

#get_wicket_delivery_numbers_array('ST Jayasuriya')



