# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype=int, skip_header=1, delimiter=',')


#Your Solution
def get_all_sixes_filter():
    
    arr=ipl_matches_array[:,16]==6
    
    return arr



