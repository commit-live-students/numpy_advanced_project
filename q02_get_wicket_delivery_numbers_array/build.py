# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    
    arr=ipl_matches_array[:,[11,20]]
    
    arr1=arr[~np.isnull(arr).any(axis=1)]
    
    arr2=arr1[:,0]
    
    
    return arr2
    




