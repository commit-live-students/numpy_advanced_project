# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np


#Your Solution
def get_all_sixes_filter():
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    runs = ipl_matches_array[:,16].astype(np.int16)
    sixes = runs==6
    return sixes

get_all_sixes_filter()

