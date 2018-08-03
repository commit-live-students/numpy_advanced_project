# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


def get_all_sixes_filter():
    
   

    bool_arr = np.array([x[16]==6 for x in ipl_matches_array])
       
    return bool_arr
#Your Solution





