# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_all_sixes_filter():
    return(ipl_matches_array[:, 16].astype(np.int16) == 6)
    
    
    
    
    
get_all_sixes_filter()



