# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_all_sixes_filter():
    runs=ipl_matches_array[:,16]
    bool_arr=runs.astype(np.int)==6
    return bool_arr

get_all_sixes_filter()  





