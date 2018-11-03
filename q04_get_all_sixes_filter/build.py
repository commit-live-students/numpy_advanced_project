# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_all_sixes_filter():
    x=np.array(ipl_matches_array[:,16])
    return list(map(lambda x: x == b'6', x))
#Your Solution


x=np.array(ipl_matches_array[:,16])
a=[1,2,3,4,5,6,7,8,9]
[b for b in x if b==b'6']
ipl_matches_array[:, 16].astype(np.int16) == 6
list(map(lambda x: x == b'6', x))


