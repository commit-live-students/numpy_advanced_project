#%load q02_get_wicket_delivery_numbers_array/build.py
import numpy as np

path='./data/ipl_matches_small.csv'

def get_wicket_delivery_numbers_array(player):
    

    arr=np.genfromtxt(path,delimiter=',',dtype='|S20',skip_header=1)
    arr1=(arr[:,20]==player)
    #print(arr[:,11:20])
    #print(arr[:,11][arr1])
    
    return arr[:,11][arr1]


get_wicket_delivery_numbers_array(b'Harbhajan Singh')



