# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_all_sixes_filter():
    six = []
    for x in ipl_matches_array:
        six.append(np.array(x[16] == b'6'))
        
    return np.array(six)
get_all_sixes_filter()



