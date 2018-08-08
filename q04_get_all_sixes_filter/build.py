# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np



#Your Solution
def get_all_sixes_filter():
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    return np.array([True if x.astype(np.int16)==6 else False for x in ipl_matches_array[0:,16]])




