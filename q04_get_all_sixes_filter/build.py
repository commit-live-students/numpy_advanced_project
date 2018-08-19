# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np

def get_all_sixes_filter():
    ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50',skip_header =1, delimiter=',')
    match_array = np.array(ipl_matches_array)
    expected_filter = (match_array[:, 16].astype(np.int16) == 6)
    return expected_filter

#Your Solution
get_all_sixes_filter()


