# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_all_sixes_filter():
    runs = ipl_matches_array[:,16].astype(int)
    array = runs == 6
    return array
    
get_all_sixes_filter()


