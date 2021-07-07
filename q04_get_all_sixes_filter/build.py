# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
path = ipl_matches_array
#Your Solution
def get_all_sixes_filter():
    runs_filter = (path[:, 16].astype(np.int16) == 6 )
    
    print(runs_filter)
    return runs_filter
get_all_sixes_filter()


